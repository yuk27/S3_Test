pipeline {
  agent any
  stages {
    stage('Run Python') {
      steps {
        sh 'python3 -m pip install boto3'
        sh 'python3 Main.py'
      }
    }

  }
}