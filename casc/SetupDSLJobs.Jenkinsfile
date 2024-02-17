pipeline {
    agent any
    stages {
        stage("Add environment values to jobs") {
            steps {
                script {
                    dir("casc/jobs") {
                        sh "sed -i 's/INPUT.PROJECT_NAME/${env.PROJECT_NAME}/g' *"
                        sh "sed -i 's/INPUT.PROJECT_URL/${env.PROJECT_URL}/g' *"
                        sh "sed -i 's/INPUT.RANDOM_INT/${env.RANDOM_INT}/g' *"
                        sh "ls * | xargs cat"
                    }
                }
            }
        }
    }
}