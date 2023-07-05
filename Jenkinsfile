pipeline {
    agent any
  
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'master', url: 'https://github.com/Safouene7/Pythonapp.git'
            }
        }
  
        stage('Build and run Docker image') {
            steps {
                sh 'docker build -t api300 .'
                sh 'docker run -d api300'
            }
        }
  
        stage('Push Docker image') {
            steps {
                script{
                   withCredentials([string(credentialsId: '2b082d82-c595-4ad3-97eb-44fbd3a19485', variable: 'dockerhubpwd')]) {
                   sh 'docker login -u safouene7 -p ${Sbng-2023}'
}
                   sh 'docker push safouene7/app:api300'
          }
        }
     }
  }
}


