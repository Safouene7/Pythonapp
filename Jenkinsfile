pipeline {
    agent any
  
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dckr_pat_BLXuDXNR_6ncvMyGoIpwVefGni4')
    }
  
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
                sh "docker login -u ${safouene7} -p ${Sbng-2023}"
                sh 'docker push safouene7/app:api300'
            }
        }
    }
}


