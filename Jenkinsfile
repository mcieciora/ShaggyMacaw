def testImage

pipeline {
    agent any
    environment {
        FLAG = getValue("FLAG", "smoke")
        TEST_GROUPS = getValue("TEST_GROUP", "all")
        REGULAR_BUILD = getValue("REGULAR_BUILD", true)
    }
    stages {
        stage ("Prepare docker test image") {
            steps {
                script {
                    testImage = docker.build("test_image:${env.BUILD_ID}", "-f automated_tests/Dockerfile .")
                }
            }
        }
        stage("Code analysis") {
            when {
                expression {
                    return env.REGULAR_BUILD == "true"
                }
            }
            parallel {
                stage ("Pylint") {
                    steps {
                        script {
                            testImage.inside("-v $WORKSPACE:/app") {
                                sh "python3 -m pylint src --max-line-length=120 --disable=C0114 --fail-under=9.5"
                                sh "python3 -m pylint --load-plugins pylint_pytest automated_tests --max-line-length=120 --disable=C0114,C0116 --fail-under=9.5"
                                sh "python3 -m pylint tools/python --max-line-length=120 --disable=C0114 --fail-under=9.5"
                            }
                        }
                    }
                }
                stage ("flake8") {
                    steps {
                        script {
                            testImage.inside("-v $WORKSPACE:/app") {
                                sh "python3 -m flake8 --max-line-length 120 --max-complexity 10 src"
                            }
                        }
                    }
                }
                stage ("ruff") {
                    steps {
                        script {
                            testImage.inside("-v $WORKSPACE:/app") {
                                sh "python3 -m ruff format ."
                                sh "python3 -m ruff check ."
                            }
                        }
                    }
                }
                stage ("black") {
                    steps {
                        script {
                            testImage.inside("-v $WORKSPACE:/app") {
                                sh "python3 -m black ."
                            }
                        }
                    }
                }
                stage("Code coverage") {
                    steps {
                        script {
                            testImage.inside("-v $WORKSPACE:/app") {
                                sh "python3 -m pytest --cov=src automated_tests/ --cov-fail-under=95 --cov-report=html"
                            }
                            publishHTML target: [
                                allowMissing: false,
                                alwaysLinkToLastBuild: false,
                                keepAll: true,
                                reportDir: "htmlcov",
                                reportFiles: "index.html",
                                reportName: "PyTestCov"
                            ]
                        }
                    }
                }
                stage ("Scan for skipped tests") {
                    when {
                        expression {
                            return env.BRANCH_NAME == "release" || env.BRANCH_NAME == "master"
                        }
                    }
                    steps {
                        script {
                            sh "python3 automated_tests/tools/python/scan_for_skipped_tests.py"
                        }
                    }
                }
            }
        }
        stage ("Run unit tests") {
            steps {
                script {
                    testImage.inside("-v $WORKSPACE:/app") {
                        sh "python3 -m pytest -m unittest -v --junitxml=results/unittests_results.xml"
                    }
                }
            }
        }
        stage("Run tests") {
            matrix {
                axes {
                    axis {
                        name "TEST_GROUP"
                        values "google"
                    }
                }
                stages {
                    stage("Test stage") {
                        steps {
                            script {
                                if (env.TEST_GROUPS == "all" || env.TEST_GROUPS.contains(TEST_GROUP)) {
                                    echo "Running ${TEST_GROUP}"
                                    testImage.inside("-v $WORKSPACE:/app") {
                                        sh "python3 -m pytest -m ${FLAG} -k ${TEST_GROUP} -v --junitxml=results/${TEST_GROUP}_results.xml"
                                    }
                                }
                                else {
                                    echo "Skipping execution."
                                }
                            }
                        }
                    }
                }
            }
        }
        stage ("Staging") {
            when {
                expression {
                    return env.REGULAR_BUILD == "true"
                }
            }
            stages {
                stage ("Build docker compose") {
                    steps {
                        script {
                            sh "docker compose build --no-cache"
                        }
                    }
                }
                stage ("Run app & health check") {
                    steps {
                        script {
                            sh "chmod +x tools/shell_scripts/app_health_check.sh"
                            sh "tools/shell_scripts/app_health_check.sh 30 1"
                        }
                    }
                    post {
                        always {
                            sh "docker compose down --rmi all -v"
                            sh "docker images"
                            sh "docker container ls -a"
                            sh "docker volume ls"
                        }
                    }
                }
                stage ("Push docker image") {
                    when {
                        expression {
                            return env.BRANCH_NAME == "master" || env.BRANCH_NAME == "develop"
                        }
                    }
                    steps {
                        script {
                            def registryPath = "http://localhost:5000"
                            if (env.BRANCH_NAME == "master") {
                                registryPath = "https://index.docker.io/v1/"
                            }
                            docker.withRegistry("${registryPath}", "dockerhub_creds") {
                                def customImage = docker.build("careless_vaquita:${BRANCH_NAME}_${env.BUILD_ID}")
                                customImage.push()
                            }
                        }
                    }
                }
                stage ("Push tag") {
                    when {
                        expression {
                            return env.BRANCH_NAME == "master"
                        }
                    }
                    steps {
                        script {
                            sh "chmod +x tools/shell_scripts/create_and_push_tag.sh"
                            sh "tools/shell_scripts/create_and_push_tag.sh ${BRANCH_NAME}_${env.BUILD_ID} ${env.BUILD_ID}"
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: "**/*.xml, htmlcov/*.html"
            junit "**/*.xml"
            sh "docker rmi test_image:${env.BUILD_ID}"
            dir("$WORKSPACE") {
                deleteDir()
            }
        }
    }
}


def getValue(variable, defaultValue) {
    return params.containsKey(variable) ? params.get(variable) : defaultValue
}