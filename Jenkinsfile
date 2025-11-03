pipeline {
    agent any   // Run on any available Jenkins agent

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm  // Jenkins auto-checks out the repo
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                // Example build command
                bat 'echo === Running Build ==='
                // or use "sh" for Linux agents: sh 'echo === Running Build ==='
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the project...'
                bat 'echo === Deploy Successful ==='
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
    }
}
