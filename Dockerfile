FROM python:3.8

WORKDIR /app
ADD ./src/ /app/

RUN  sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list \
    && sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -i https://mirrors.aliyun.com/pypi/simple/ --upgrade pip \
    && pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /app/requirements.txt \
    && rm -rf /app/requirements.txt

ENTRYPOINT [ "python3", "main.py" ]