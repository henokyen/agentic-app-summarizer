pipeline {
    agent any
    environment {
        AWS_REGION = 'us-east-2'
        AWS_ACCOUNT_ID = '319994344936'
        ECR_REPO = 'agentic-app-summarizer'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        IMAGE_URI
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
                    docker compose --version
                    aws --version || echo "AWS CLI not found
                    '''
                }
            }
        }
    }
}