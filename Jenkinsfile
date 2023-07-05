pipeline {
    agent any
  
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'master', url: 'https://github.com/Safouene7/Pythonapp.git'
            }
        }
  
        stage('Run API') {
            steps {
                sh 'sudo apt-get install -y python3'
                sh 'sudo apt install python3-pip -y'

                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 api.py'
            }
        }
  
        stage('Build and run Docker image') {
            steps {
                sh 'docker build -t api300 .'
                sh 'docker run -d api300'
            }
        }
    }
}

