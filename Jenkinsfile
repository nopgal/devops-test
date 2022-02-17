pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        
         stage('docker build') {
            steps {
                echo "docker build -t python_update_str ."
                bat(returnStdout: true, script: "docker build -t python_update_str .")
            }
        }
    }
   
}
