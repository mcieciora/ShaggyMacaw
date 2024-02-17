pipeline {
    agent any
    parameters {
        string(name: 'PROJECT_NAME', defaultValue: 'CarelessVaquita', description: "Project name.")
        string(name: 'PROJECT_URL', defaultValue: 'https://github.com/mcieciora/CarelessVaquita.git', description: "Full github url to repository.")
        string(name: 'RANDOM_INT', defaultValue: '00000000', description: "Random 8 numbers integer.")
    }
    stages {
        stage("Add environment values to jobs") {
            steps {
                script {
                    dir("casc/jobs") {
                        sh "sed -i 's~INPUT.PROJECT_NAME~${env.PROJECT_NAME}~g' *"
                        sh "sed -i 's~INPUT.PROJECT_URL~${env.PROJECT_URL}~g' *"
                        sh "sed -i 's~INPUT.RANDOM_INT~${env.RANDOM_INT}~g' *"
                        sh "ls * | xargs cat"
                    }
                    jobDsl targets: 'casc/jobs/*'
                }
            }
        }
    }
}