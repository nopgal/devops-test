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
        
         stage('docker build') {
            steps {
                echo "docker build -t python_update_str ."
                bat(returnStdout: true, script: "docker run -p 5000:5000 -d update_str_img")
            }
        }
        
    }
   
}
