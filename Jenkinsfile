pipeline {
  agent any
  stages {
    stage('Run Python') {
      steps {
        sh '''echo "S3_CREDENTIALS" :: $S3_CREDENTIALS
echo "USER_CREDENTIALS_USR" :: $USER_CREDENTIALS_USR
echo "USER_CREDENTIALS_PSW" :: $USER_CREDENTIALS_PSW
echo "BUILD_NUMBER" :: $BUILD_NUMBER
echo "BUILD_ID" :: $BUILD_ID
echo "BUILD_DISPLAY_NAME" :: $BUILD_DISPLAY_NAME
echo "JOB_NAME" :: $JOB_NAME
echo "JOB_BASE_NAME" :: $JOB_BASE_NAME
echo "BUILD_TAG" :: $BUILD_TAG
echo "EXECUTOR_NUMBER" :: $EXECUTOR_NUMBER
echo "NODE_NAME" :: $NODE_NAME
echo "NODE_LABELS" :: $NODE_LABELS
echo "WORKSPACE" :: $WORKSPACE
echo "JENKINS_HOME" :: $JENKINS_HOME
echo "JENKINS_URL" :: $JENKINS_URL
echo "BUILD_URL" ::$BUILD_URL
echo "JOB_URL" :: $JOB_URL
'''
        sh 'python3 -m pip install boto3'
        sh 'python3 Main.py'
      }
    }

  }
  environment {
    USER_CREDENTIALS = credentials('S3_CREDENTIALS')
  }
}