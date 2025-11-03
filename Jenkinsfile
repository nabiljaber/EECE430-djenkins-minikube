pipeline {
  agent any
  triggers { pollSCM('H/2 * * * *') }  // ~every 2 min
  stages {
    stage('Checkout'){ steps { git branch: 'main', url: 'https://github.com/<you>/EECE430-djenkins-minikube.git' } }
    stage('Use Minikube Docker'){ steps { bat 'minikube docker-env --shell=cmd > mk_env.bat && call mk_env.bat' } }
    stage('Build Image'){ steps { bat 'docker build -t mydjangoapp:latest .' } }
    stage('Deploy'){ steps {
      bat 'minikube kubectl -- apply -f deployment.yaml'
      bat 'minikube kubectl -- apply -f service.yaml'
      bat 'minikube kubectl -- rollout status deployment/django-deployment'
      bat 'minikube kubectl -- exec deploy/django-deployment -- python manage.py migrate --noinput'
    }}
  }
}
