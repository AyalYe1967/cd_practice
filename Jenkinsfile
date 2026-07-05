pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "start build step.."
                script {
                    // שימוש בתוסף - תקין!
                    docker.build("my-app:latest")
                }
                echo "finish build step"
            }
        }

        stage('Test') {
            steps {
                echo "start first test steps"
                sh "pytest"
                echo "done test.."
            }
        }

        stage('Push to ecr') {
            steps {
                script {
                    // משתנים מקומיים לשלב ה-Push
                    def awsAccountId = '992382545251'
                    def awsRegion    = 'us-east-1'
                    def ecrRepo      = 'a_y/cd'
                    def imageTag     = "v${env.BUILD_NUMBER}"
                    def ecrUrl       = "${awsAccountId}.dkr.ecr.${awsRegion}.amazonaws.com"

                    echo "Logging in and pushing to ECR using Jenkins Docker Plugin..."
                    
                    // שימוש בתוסף הנייטיב של ג'נקינס כדי לעשות Push ללא פקודת docker במערכת
                    // הערה: נדרש להגדיר Credentials בג'נקינס עבור ה-AWS Access Key אם השרת לא מחובר ל-IAM Role
                    docker.withRegistry("https://${ecrUrl}") {
                        def myImage = docker.image("my-app:latest")
                        myImage.push(imageTag)
                        myImage.push("latest")
                    }
                }
            }
        }
    }
}
