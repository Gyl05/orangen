pipeline{
    agent any
    stages{
        stage('Build-image'){
            when{
                changeset 'html/*'
            }
            steps{
                withCredentials([usernamePassword(credentialsId: 'jenkins-to-Aliyun-dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]){
                    sh """
                        podman build -t registry.cn-hongkong.aliyuncs.com/fruitbucket/orangen:latest -f dockerfile1 .
                        echo ${DOCKER_PASSWORD} | podman login --username=gyl2021 --password-stdin registry.cn-hongkong.aliyuncs.com
                        podman push registry.cn-hongkong.aliyuncs.com/fruitbucket/orangen:latest
                    """
                }
            }
        }
        stage('deployment'){
            when{
                    changeset 'html/*'
            }
            steps{
                sh """
                    echo '部署镜像 docker-compose or k8s.'
                """
            }
        }
    }
}