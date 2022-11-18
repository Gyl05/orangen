pipeline{
    agent {
        label 'orangen-slave'
    }
    stages{
        stage('Build-image'){
            when{
                changeset 'html/*'
            }
            steps{
                withCredentials([usernamePassword(credentialsId: 'jenkins-to-Aliyun-dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]){
                    sh """
                        docker build -t registry.cn-hongkong.aliyuncs.com/fruitbucket/orangen:latest -f dockerfile1 .
                        echo ${DOCKER_PASSWORD} | podman login --username=gyl2021 --password-stdin registry.cn-hongkong.aliyuncs.com
                        docker push registry.cn-hongkong.aliyuncs.com/fruitbucket/orangen:latest
                    """
                }
            }
        }
        stage('deployment'){
            when{
                anyOf {
                    changeset 'html/*'
                    changeset 'Jenkinsfile'
                } 
            }
            steps{
                sh """
                    echo '部署镜像 docker-compose or k8s.'
                    pwd
                    whoami
                    docker pull registry.cn-hongkong.aliyuncs.com/fruitbucket/orangen:latest
                    docker run -it --rm -p0.0.0.0:80:80 registry.cn-hongkong.aliyuncs.com/fruitbucket/orangen:latest
                """
            }
        }
    }
}