pipeline {
    agent any

    stages {
        stage('Git pull') {
            steps {
                git branch: 'main', url: 'https://github.com/Safouene7/Pythonapp.git'
            }
        }

        stage('Execute Python File') {
            steps {
                dir('python') {
                    sh 'python app-saf.py'
                }
            }
        }
    }
}
