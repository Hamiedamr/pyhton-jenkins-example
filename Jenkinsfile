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
         stage('Docker') {
            steps {
                script {
                    def dockerImage = docker.build("abdelhamiedamr/jenkins_image")
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}

