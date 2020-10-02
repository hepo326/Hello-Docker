pipeline {
     environment { 
        registry = "mohebbadawy/hello-docker" 
        registryCredential = 'dockerhub' 
        awsCredential = 'aws-eks' 
        cluster = 'hello-docker-cluster' 
        region = 'us-west-2'
        dockerImage = '' 
        imageVersion = '1.0' 
    }

	agent any
	stages {

    stage('Lint') {
        steps {
            sh 'tidy -q -e src/templates/*.html'
        }
    }

    stage('Detect Deployment Type') { 
        steps { 
            script { 
                
                if (env.BRANCH_NAME == 'development' || env.CHANGE_TARGET == 'development') {
                       env.DEPLOYMENT_TYPE = 'blue'
                 }
                
                
                else if (env.BRANCH_NAME == 'master' || env.CHANGE_TARGET == 'master') {
                       env.DEPLOYMENT_TYPE = 'green'
                 }
    
            }
        } 
        
        }

    stage('Building Docker Image') { 
        steps { 
            script { 
                
                dockerImage = docker.build ('${registry}:${imageVersion}')
                docker.withRegistry( '', registryCredential ) { 
                    dockerImage.push() 
                
                }
                }
            } 
        }

    stage('Deployment') {
        steps {
            withAWS(region: region, credentials: awsCredential) {
                sh '''
		    aws s3 ls
                    aws eks --region ${region} update-kubeconfig --name  ${cluster}
                    kubectl config use-context arn:aws:eks:${region}:123607427500:cluster/${cluster}
		    kubectl get svc
                    kubectl apply -f ./${DEPLOYMENT_TYPE}-deployment.yml
                    docker image rm ${registry}:${imageVersion}

                '''
               }
             }
		}
  

    }
}
