pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh './venv/bin/pytest test_calculator.py -v --junitxml=report.xml --cov=calculator --cov-report=xml:coverage.xml'
            }
        }
    }

    post {
        always {
            junit 'report.xml'
            cleanWs()
        }
        success {
            echo '✅ All tests passed!'
        }
        failure {
            echo '❌ Some tests failed.'
        }
    }
}
