pipeline {
	agent any
	stages
	{
		stage('Build') {
			steps {
				script {
					sh "docker build -t buzz ."
				}
			}
		}

		stage('Run') {
			steps {
				script {
					sh "docker run -itd -p 5000:5000 --name buzz buzz:latest"
				}
			}
		}

		stage('Test') {
			steps {
				script {
					sh "python3 -m pytest -v test-generator.py"
				}
			}
		}
	}
}
