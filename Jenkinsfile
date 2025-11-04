pipeline {
  agent any
  triggers { pollSCM('H/2 * * * *') }

  stages {
    // Remove Checkout stage when job is "Pipeline script from SCM"
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
