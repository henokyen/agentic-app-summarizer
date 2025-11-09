pipeline {
    agent any
    environment {
        AWS_REGION = 'us-east-2'
        AWS_ACCOUNT_ID = '319994344936'
        ECR_REPO = 'summarizer_app'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        IMAGE_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Environment'){
            steps {
                script {
                    echo "Setting up build ennviroments"
                    sh '''
                    docker --version
                    '''
                }
            }
        }
        stage('Build Docker Image'){
            steps {
                echo "Building Docker Image: ${IMAGE_URI}"
                sh '''
                docker compose build --no-cache
                dcokcer images | grep agnetic-app-summarizer
                ''' 
            }
        }
        stage ("Tag Image for ECR"{
            steps {
                echo "Tagging image for ECR: ${IMAGE_URI}"
                sh '''
                docker tag agentic-app-summarizer:latest ${IMAGE_URI}
                docker images | grep ${ECR_REPO}
                '''
            }
        })
    }
}