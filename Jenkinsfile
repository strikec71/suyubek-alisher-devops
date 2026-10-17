pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
        disableConcurrentBuilds()
        timeout(time: 15, unit: 'MINUTES')
    }
    environment {
        STUDENT_NAME = 'Alisher'
        STUDENT_SURNAME = 'Suyubek'
        STUDENT_GROUP = 'IT2-2306'
        STUDENT_ID = '37773'
        IMAGE_NAME = 'suyubek-alisher-devops'
        CONTAINER_NAME = 'suyubek-alisher-container'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh '''
                    set -eu
                    printf 'Student: %s %s\nGroup: %s\nStudent ID: %s\n' \
                      "$STUDENT_SURNAME" "$STUDENT_NAME" "$STUDENT_GROUP" "$STUDENT_ID"
                    printf 'Git commit: '
                    git rev-parse HEAD
                '''
            }
        }
        stage('Build') {
            steps { sh 'python3 -m compileall -q app tests' }
        }
        stage('Test') {
            steps { sh "python3 -m unittest discover -s tests -p 'test_*.py' -v" }
        }
        stage('Docker Build') {
            steps {
                sh '''
                    set -eu
                    docker build --label "org.opencontainers.image.revision=$(git rev-parse HEAD)" \
                      -t "$IMAGE_NAME" .
                '''
            }
        }
        stage('Docker Run') {
            steps {
                sh '''
                    set -eu
                    if docker container inspect "$CONTAINER_NAME" >/dev/null 2>&1; then
                        docker rm -f "$CONTAINER_NAME"
                    fi
                    docker run -d --name "$CONTAINER_NAME" \
                      -p 127.0.0.1:8000:8000 \
                      -e STUDENT_NAME -e STUDENT_SURNAME -e STUDENT_GROUP -e STUDENT_ID \
                      "$IMAGE_NAME"
                    if ! python3 -m scripts.check_running; then
                        docker logs "$CONTAINER_NAME"
                        exit 1
                    fi
                    docker logs "$CONTAINER_NAME"
                    docker ps --filter "name=^/${CONTAINER_NAME}$"
                    docker image inspect "$IMAGE_NAME" \
                      --format '{{index .Config.Labels "org.opencontainers.image.revision"}}'
                '''
            }
        }
    }
    post {
        failure { echo 'Pipeline failed. Read the failed stage; subsequent stages are not successful.' }
        success { echo 'Suyubek Alisher DevOps workflow completed successfully.' }
    }
}
