pipeline {
    agent any

    environment {
        IMAGE_NAME = "devops-task-api"
        IMAGE_TAG = "1.${BUILD_NUMBER}"
        DOCKER_USER = "akifmhd"
        FULL_IMAGE = "${DOCKER_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
        TRIVY_CACHE_DIR = "${WORKSPACE}/.trivy_cache"
        REPORTS_DIR = "${WORKSPACE}/reports"

    }

    stages {
        stage('Cloning repository') {
            steps {
                git branch: 'mainv1', changelog: false, poll: false, url: 'https://github.com/x091204/DevOps-Task-API.git'
                sh "pwd"
            
            }
        }
        stage('Build') {
            steps {
                sh """
                    pwd
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements-dev.txt
                """
            }
        }
        stage('Test') {
            steps {
                sh """
                    . venv/bin/activate
                    pytest tests/
                """

            }
        }
        stage('Docker build') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }
        stage('Trivy scan') {
            steps {

                sh "mkdir -p ${TRIVY_CACHE_DIR} ${REPORTS_DIR} trivy"
                sh "wget https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl -O trivy/html.tpl"
                sh "trivy --version"
                sh """
                trivy image \
                --cache-dir ${TRIVY_CACHE_DIR} \
                --severity HIGH,CRITICAL \
                --ignore-unfixed \
                --ignorefile .trivyignore \
                --format template \
                --template @trivy/html.tpl \
                --output ${REPORTS_DIR}/trivy-image.html \
                --exit-code 1 \
                ${IMAGE_NAME}:${IMAGE_TAG}
                """

                

                
            }
        }
        stage('Docker tag and push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'akifmhd',
                    passwordVariable: 'Dockerhubpass',
                    usernameVariable: 'Dockerhubusername'
                      )]) {
                    sh """
                        echo "$Dockerhubpass" | docker login -u "$Dockerhubusername" --password-stdin
                        docker tag devops-task-api:${IMAGE_TAG} ${DOCKER_USER}/devops-task-api:${IMAGE_TAG}
                        docker push ${DOCKER_USER}/devops-task-api:${IMAGE_TAG}
                     """
                }
            }
        }
        stage('Deploy') {
            steps {
                sh """
                    docker stop devops-app || true
                    docker rm devops-app || true
                    docker run -d -p 5000:5000 --name devops-app ${FULL_IMAGE}
                """
            }
        }
    }

    post {

    always {
        archiveArtifacts artifacts: 'reports/*', allowEmptyArchive: true
        cleanWs( patterns: [[pattern: '.trivy_cache/**', type: 'EXCLUDE']])
        sh """
                docker image prune -f
                docker images ${IMAGE_NAME} --format "{{.Tag}}" | sort -r | tail -n +4 | xargs -I {} docker rmi ${IMAGE_NAME}:{} || true
            """
        }
        success { echo "Build ${BUILD_NUMBER} passed — image pushed as ${FULL_IMAGE}" }
        failure { echo "Build ${BUILD_NUMBER} failed — check Trivy report in artifacts" }
    }
}
