pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'dockerhub-cred'
        IMAGE_NAME = '3booda24/flasktest56480:latest'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'Master',
                    url: 'https://github.com/abdelrahmanonline4/FLASK-APP.git'
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME} .
                '''
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: "${DOCKER_CREDENTIALS_ID}",
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh '''
                        echo "${DOCKER_PASSWORD}" | docker login \
                            -u "${DOCKER_USERNAME}" \
                            --password-stdin
                    '''
                }
            }
        }

        stage('Docker Push') {
            steps {
                sh '''
                    docker push ${IMAGE_NAME}
                '''
            }
        }
    }
}
