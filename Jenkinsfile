pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out the code from Git.
                //git 'git@github.com:czarnycap/node-app.git'
                 checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/czarnycap/node-app']]])
            }
        }
        stage('Build') {
            steps {
                // Build the Node.js application.
                sh 'npm install'
                /*sh 'npm run build'*/
            }
        }
        stage('Test') {
            steps {
                // Run the tests for the Node.js application.
                sh 'npm test'
            }
        }
        stage('SonarQube') {
            steps {
                sh 'sonar-scanner -Dsonar.projectKey=node-js-api-app -Dsonar.sources=. -Dsonar.host.url=http://192.168.16.154:9000 -Dsonar.login=e996d49bf3a066bf7c2077529aa8ed4481b6e0ca'
            }
                
        }
        stage('Archive artifacts') {
            //configuration is stored in node-js app
            steps {
                echo "Build number is ${currentBuild.number}"
                sh "npm publish --tag Build-${currentBuild.number}"
            }

        }
        stage('Deploy') {
            steps {
                // Build the Docker image for the Node.js application.
                sh 'docker build -t my-nodejs-app .'

                // Run the Docker image.
                sh 'docker run --rm -d -p 3000:3000 my-nodejs-app'
                sh 'docker ps|grep my-nodejs-app'
            }
        }
    }
}
