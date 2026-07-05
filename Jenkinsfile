pipeline {
    agent any

    stages{
        stage('Build'){
            steps {
                echo "start build step.."
                sh "docker build -t my-app:latest ."
                echo "finish build step"
                }
        }

        stage('Test'){
            steps {
                echo "start first test steps"
                sh "pytest"
                echo "done test.."
            }
        }

        stage('Push to ecr') { 
            environment {
               AWS_ACCOUNT_ID = '992382545251'
               AWS_REGION     = 'us-east-1'
               ECR_REPO       = 'a_y/cd'
               IMAGE_TAG      = "v${BUILD_NUMBER}" 
            }
                    steps {
                        sh "aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
        
                        sh "docker tag my-app:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}"
        
                        sh "docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}"
                    }
                }
