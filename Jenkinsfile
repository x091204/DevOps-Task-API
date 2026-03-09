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
        stage('Docker tag and push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'akifmhd', passwordVariable: 'Dockerhubpass', usernameVariable: 'Dockerhubusername')]) {
                    sh '''
                        echo "$Dockerhubpass" | docker login -u "$Dockerhubusername" --password-stdin
                        docker tag devops-task-api:1.0 akifmhd/devops-task-api:1.0
                        docker push akifmhd/devops-task-api:1.0
                     '''
                }
            }
        }
        stage('Docker Run') {
            steps {
                sh '''
                    docker stop devops-app || true
                    docker rm devops-app || true
                    docker run -d -p 5000:5000 --name devops-app devops-task-api:1.0
                '''
            }
        }
    }

    post {

    always {
        cleanWs()
        sh 'docker image prune -f'
        }
    success {
        echo 'Pipeline completed successfully!'
        }
    failure {
        echo 'Pipeline failed!'
        }
    }
}
