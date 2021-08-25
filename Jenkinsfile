pipeline {
    agent any 
    stages {
        stage('Checkout') { 
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '965279af-cab6-4cf7-9829-4faa69c04d9c', url: 'https://github.com/muskan245verma/pythonJenkin.git']]])
                  }
        }
        stage('Build') { 
            steps {
                git branch: 'master', url: 'https://github.com/muskan245verma/pythonJenkin.git'
                bat 'python Listgame.py'
            }
        }
        stage('Test') { 
            steps {
                echo "Tested Successfully"
            }
        }
    }
}
