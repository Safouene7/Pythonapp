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
                     withCredentials([usernamePassword(credentialsId: 'd3427c3c-dc64-4d8e-b4aa-59440db6f55e', usernameVariable: 'saf', passwordVariable: '1234')]) {
                         sh 'docker login -u safouene7 -p Sbng-2023'
}
                   sh 'docker tag api300 safouene7/app:latest'
                   sh 'docker push safouene7/app:latest'
          }
        }
     }
  }
}


