def customImage

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
                    customImage = docker.build("test_image:${env.BUILD_ID}", "-f automated_tests/Dockerfile .")
                }
            }
        }
        stage("Code analysis") {
            when {
                expression {
                    return env.REGULAR_BUILD == true
                }
            }
            parallel {
                stage ("Pylint") {
                    steps {
                        script {
                            customImage.inside("-v $WORKSPACE:/app") {
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
                            customImage.inside("-v $WORKSPACE:/app") {
                                sh "python3 -m flake8 --max-line-length 120 --max-complexity 10 src"
                            }
                        }
                    }
                }
                stage ("ruff") {
                    steps {
                        script {
                            customImage.inside("-v $WORKSPACE:/app") {
                                sh "python3 -m ruff format ."
                                sh "python3 -m ruff check ."
                            }
                        }
                    }
                }
                stage ("black") {
                    steps {
                        script {
                            customImage.inside("-v $WORKSPACE:/app") {
                                sh "python3 -m black ."
                            }
                        }
                    }
                }
                stage("Code coverage") {
                    steps {
                        script {
                            customImage.inside("-v $WORKSPACE:/app") {
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
            }
        }
        stage ("Run unit tests") {
            steps {
                script {
                    customImage.inside("-v $WORKSPACE:/app") {
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
                                if (env.TEST_GROUP == "all" || env.TEST_GROUPS.contains(TEST_GROUP)) {
                                    echo "Running ${TEST_GROUP}"
                                    customImage.inside("-v $WORKSPACE:/app") {
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
                    return env.REGULAR_BUILD == true
                }
            }
            parallel {
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
    }
    post {
        always {
            archiveArtifacts artifacts: "**/*.xml, htmlcov/*.html"
            junit "**/*.xml"
            dir("$WORKSPACE") {
                deleteDir()
            }
        }
    }
}


def getValue(variable, defaultValue) {
    return params.containsKey(variable) ? params.get(variable) : defaultValue
}