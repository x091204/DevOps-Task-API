pipeline {
    agent any

    environment {
        IMAGE_NAME = "devops-task-api"
        IMAGE_TAG = "1.${BUILD_NUMBER}"
        DOCKER_USER = "akifmhd"
    }

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
                    pip install -r requirements-dev.txt
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
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }
        stage('Docker tag and push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'akifmhd', passwordVariable: 'Dockerhubpass', usernameVariable: 'Dockerhubusername')]) {
                    sh '''
                        echo "$Dockerhubpass" | docker login -u "$Dockerhubusername" --password-stdin
                        docker tag devops-task-api:${IMAGE_TAG} ${DOCKER_USER}/devops-task-api:${IMAGE_TAG}
                        docker push ${DOCKER_USER}/devops-task-api:${IMAGE_TAG}
                     '''
                }
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    docker stop devops-app || true
                    docker rm devops-app || true
                    docker run -d -p 5000:5000 --name devops-app ${DOCKER_USER}/${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }
    }

    post {

    always {
        cleanWs()
        sh '''
                docker image prune -f
                docker images ${IMAGE_NAME} --format "{{.Tag}}" | sort -r | tail -n +4 | xargs -I {} docker rmi ${IMAGE_NAME}:{} || true
            '''
        }
    success {
        echo 'Pipeline completed successfully!'
        }
    failure {
        echo 'Pipeline failed!'
        }
    }
}
