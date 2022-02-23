pipeline {
    agent any

    stages {
        
         stage('docker build') {
            steps {
                echo "docker build -t python_update_str ."
                bat(returnStdout: true, script: "docker build -t python_update_str .")
            }
        }
        
        stage('docker stop old container image') {
            steps {
                echo "docker stop \$(docker ps -q --filter ancestor=update_str_img )"
                powershell(returnStdout: true, script: "docker stop \$(docker ps -q --filter ancestor=update_str_img )")
            }
        }             
        
         stage('docker run') {
            steps {
                echo "docker run -p 5000:5000 -d update_str_img"
                bat(returnStdout: true, script: "docker run -p 5000:5000 -d update_str_img")
            }
        }
        
    }
   
}
