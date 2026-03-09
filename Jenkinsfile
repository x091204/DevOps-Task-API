pipeline {
    agent { label "worker-nod" }

    stages {
        stage('Cloning repository') {
            steps {
                git branch: 'main', changelog: false, poll: false, url: 'https://github.com/x091204/DevOps-Task-API.git'
                sh "pwd"
            
            }
        }
        stage('Build') {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
        stage('Test') {
            steps {
                sh "p"
            }
        }
    }
}