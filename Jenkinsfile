pipeline {
    agent  any
 
    stages {
        stage('setup environment') {
            steps {
                sh hostname 
            }
        }        
        stage('Checkout') {
            steps {
                echo 'get latest codebase' 
            }
        }
        stage('Build') {
            steps {
                echo "build or compile"
            }
        }
        stage('Test') {
            steps {
                echo "test sonnar scanner"
            }
        }
        stage('Package'){
            steps {
                echo "put to Nexus"
            }
        }
    }
}
