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
  }
}

