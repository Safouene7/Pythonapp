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
                     withCredentials([usernamePassword(credentialsId: '4a2ef18d-42ef-454d-9531-dda2aff3c9af', usernameVariable: 'saf', passwordVariable: '1234')]) {
}
                   sh 'docker push api300'
          }
        }
     }
  }
}


