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
                   withCredentials([string(credentialsId: 'Sbng-2023', variable: 'Sbng-2023')]) {
                   sh 'docker login -u safouene7 -p ${dockerhubpwd}'
}
                   sh 'docker push safouene7/app:api300'
          }
        }
     }
  }
}


