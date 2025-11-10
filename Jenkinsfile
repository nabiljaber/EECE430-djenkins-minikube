pipeline {
  agent any
  triggers { pollSCM('H/2 * * * *') }

  stages {
    stage('Checkout + Clean') {
      steps {
        deleteDir()
        git branch: 'main', url: 'https://github.com/nabiljaber/EECE430-djenkins-minikube.git'
      }
    }

    stage('Verify Tooling') {
      steps {
        bat '''
        where minikube
        minikube version
        where docker
        docker version
        minikube status
        '''
      }
    }

    stage('Build Image in Minikube') {
      steps {
        bat '''
        call minikube docker-env --shell=cmd > mk_env.bat
        call mk_env.bat
        docker build -t mydjangoapp:latest .
        '''
      }
    }

    stage('Deploy & Migrate') {
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
