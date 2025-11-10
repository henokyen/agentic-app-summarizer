pipeline {
    agent any
    environment {
        AWS_REGION = 'us-east-2'
        AWS_ACCOUNT_ID = '319994344936'
        ECR_REPO = 'summarizer_app'
        IMAGE_TAG = "latest"
        COMPOSE_PROJECT_NAME = 'agentic_app'
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
                    echo "Setting up build enviroments"
                    sh '''
                    docker --version
                    aws --version
                    '''
                }
            }
        }
        stage('Build Docker Image'){ //{COMPOSE_PROJECT_NAME}-{service_name}:tag
            steps {
                echo "Building Docker Image: ${IMAGE_URI}"
                sh '''
                docker compose build --no-cache
                docker images | grep agentic
                ''' 
            }
        }
        stage ("Tag Image for ECR"){
            steps {
                echo "Tagging image for ECR: ${IMAGE_URI}"
                sh '''
                docker tag ${COMPOSE_PROJECT_NAME}-agentic-app-summarizer ${IMAGE_URI}
                docker images | grep ${ECR_REPO}
                '''
            }
        }
        stage('AWS ECR Login') {
            steps {
                echo 'Logging into AWS ECR...'
                withCredentials([
                    [
                        $class: 'AmazonWebServicesCredentialsBinding',
                        credentialsId: 'aws-credentials', // Jenkins credential ID
                        accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                        secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                    ]
                ]) {
                    script {
                        sh '''
                            # Login to ECR
                            aws ecr get-login-password --region ${AWS_REGION} | \
                            docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
                            # Verify ECR repository exists
                            aws ecr describe-repositories --repository-names ${ECR_REPOSITORY} --region ${AWS_REGION}
                        '''
                    }
                }
            }
        }
         stage('Push to ECR') {
            steps {
                echo 'Pushing Docker image ${IMAGE_URI} to ECR...'
                script {
                    sh '''
                        # Push with build number tag
                        docker push ${IMAGE_URI}
                        echo "Successfully pushed images:"
                        echo "  ${IMAGE_URI}"
                    '''
                }
            }
        }
    }
}