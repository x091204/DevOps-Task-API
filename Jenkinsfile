pipeline {
    agent any

    stages {
        stage('Cloning repository') {
            steps {
                git branch: 'main', changelog: false, poll: false, url: 'https://github.com/x091204/DevOps-Task-API.git'
                sh "pwd"
            
            }
        }
        stage('Build') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/
                '''

            }
        }
        stage('Docker build') {
            steps {
                sh "docker build -t devops-task-api:1.0 ."
            }
        }
        stage('Docker Run') {
            steps {
                sh 'docker run -d -p 5000:5000 --name devops-app devops-task-api:1.0'
            }
        }
    }
}
