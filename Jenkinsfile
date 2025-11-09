pipeline {
    agent any
    environment {
        AWS_REGION = 'us-east-2'
        AWS_ACCOUNT_ID = '319994344936'
        ECR_REPO = 'agentic-app-summarizer'
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
                    aws --version || echo "AWS CLI not found"
                    '''
                }
            }
        }
    }
}