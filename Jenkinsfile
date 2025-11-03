pipeline {
  agent any
  triggers { pollSCM('H/2 * * * *') } // every ~2 minutes

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/nabiljaber/EECE430-Lab4.git'
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        bat '''
        REM === Switch Docker to Minikube Docker ===
        call minikube docker-env --shell=cmd > docker_env.bat
        call docker_env.bat

        REM === Build Django image inside Minikube Docker ===
        docker build -t mydjangoapp:latest .
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat '''
        REM === Apply updated deployment ===
        kubectl apply -f deployment.yaml

        REM === Wait for rollout ===
        kubectl rollout status deployment/django-deployment
        '''
      }
    }
  }
}
