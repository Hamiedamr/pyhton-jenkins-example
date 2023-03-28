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
              sh '''python3 -m pip install -r requirements.txt
                    python3 app.py'''
            }
        }
    }
}
