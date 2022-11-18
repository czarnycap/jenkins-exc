pipeline {
    agent {
	docker { image 'node:16.13.1-alpine' }
} 
    stages {
        stage('Build environment') {
            steps {
                echo 'get latest codebase' 
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
