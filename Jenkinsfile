pipeline{
    agent any
    stages{
        stage('Build-image'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'jenkins-to-Aliyun-dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]){
                    sh """
                        echo ${DOCKER_PASSWORD} | podman login --username=gyl2021 registry.cn-hongkong.aliyuncs.com
                        podman build -t registry.cn-hongkong.aliyuncs.com/fruitbucket/orangen:latest
                        podman push registry.cn-hongkong.aliyuncs.com/fruitbucket/orangen:latest
                    """
                }
            }
        }
    }
}