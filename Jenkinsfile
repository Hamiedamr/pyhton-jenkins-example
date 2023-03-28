pipeline {
    agent any
    stages {
    stage('Checkout') {
            steps {
               checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Hamiedamr/pyhton-jenkins-example']])
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}
