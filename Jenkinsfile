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
                withCredentials([
                    usernamePassword(credentialsId: 'dckr_pat_L5L8ySCLxfnCLGcSqy12eZS4J68', usernameVariable: 'safouene7', passwordVariable: 'Sbng-2023')
                ]) {
                    script {
                        def dockerhubCredentials = usernamePassword('dckr_pat_L5L8ySCLxfnCLGcSqy12eZS4J68')
                        def dockerhubUsername = dockerhubCredentials.username
                        def dockerhubPassword = dockerhubCredentials.password

                        sh 'docker login -u ${safouene7} -p ${Sbng-2023}'
                        sh 'docker push api300'
                    }
                }
            }
        }
    }
}

