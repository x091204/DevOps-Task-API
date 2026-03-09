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
                sh "pytest"
            }
        }
        stage('Docker build') {
            steps {
                sh "docker build -t devops-tak-api:1.0 ."
            }
        }
        stage('Docker Run') {
            steps {
                sh 'docker run --rm devops-task-api:1.0'
            }
        }
    }
}
