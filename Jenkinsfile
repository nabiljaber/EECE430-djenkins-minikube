pipeline {
  agent any
  triggers { pollSCM('H/2 * * * *') }

  stages {
    stage('Checkout (fresh)') {
      steps {
        deleteDir()
        git branch: 'main', url: 'https://github.com/nabiljaber/EECE430-djenkins-minikube.git'
        bat 'del /f /q "%WORKSPACE%\\minikube" 2>nul'
      }
    }

    stage('Ensure Minikube up') {
      steps {
        bat '''
        where minikube
        where docker
        minikube status || minikube start --driver=docker --kubernetes-version=v1.34.0 --memory=6000 --cpus=2 --disk-size=20g
        minikube status
        '''
      }
    }

    stage('Build image in Minikube') {
      steps {
        bat '''
        call minikube docker-env --shell=cmd > mk_env.bat
        call mk_env.bat
        docker version
        docker build -t mydjangoapp:latest .
        '''
      }
    }

    stage('Deploy & migrate') {
      steps {
        bat '''
        minikube kubectl -- apply -f deployment.yaml
        minikube kubectl -- apply -f service.yaml
        minikube kubectl -- rollout restart deployment/django-deployment
        minikube kubectl -- rollout status deployment/django-deployment
        minikube kubectl -- exec deploy/django-deployment -- python manage.py migrate --noinput
        '''
      }
    }
  }
}
