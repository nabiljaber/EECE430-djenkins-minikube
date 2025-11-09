pipeline {
  agent any
  triggers { pollSCM('H/2 * * * *') }

  stages {
    stage('Checkout + Clean') {
      steps {
        deleteDir() // clean workspace
        git branch: 'main', url: 'https://github.com/<your-username>/EECE430-djenkins-minikube.git'
        bat 'git fetch --all'
        bat 'git reset --hard origin/main'
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
        minikube kubectl -- rollout status deployment/django-deployment
        minikube kubectl -- exec deploy/django-deployment -- python manage.py migrate --noinput
        '''
      }
    }
  }
}
