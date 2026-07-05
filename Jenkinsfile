pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "start build step.."
                sh "docker build -t my-app:latest ."
                echo "finish build step"
            }
        }

        stage('Test') {
            steps {
                echo "start first test steps"
                sh 'docker run --rm my-app:latest pytest'
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
                withCredentials([
                    usernamePassword(
                        credentialsId: '5325e1d2-8bc7-46b5-b73b-095fccb1e0e6',
                        usernameVariable: 'AWS_ACCESS_KEY_ID',
                        passwordVariable: 'AWS_SECRET_ACCESS_KEY'
                        )
                    ]) {
                        sh "aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"

                        sh "docker tag my-app:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}"

                        sh "docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}"
                   }
        }
    }
   }
}
