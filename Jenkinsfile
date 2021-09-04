pipeline {
    agent {
        docker { image 'python:3' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'python -V'
            }
        }
    }
}