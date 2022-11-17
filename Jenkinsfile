pipeline{
    agent any
    stages{
        stage('Build-image'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'jenkins-to-Aliyun-dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]){
                    sh """
                        podman build -t registry.cn-hongkong.aliyuncs.com/fruitbucket/orangen:latest .
                        echo ${DOCKER_PASSWORD} | podman login --username=gyl2021 --password-stdin registry.cn-hongkong.aliyuncs.com
                        podman push registry.cn-hongkong.aliyuncs.com/fruitbucket/orangen:latest
                    """
                }
            }
        }
    }
}