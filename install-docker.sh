#!/bin/bash

echo "Starting..."
apt update
apt install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common -y

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

apt-key fingerprint 0EBFCD88

add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"

add-apt-repository ppa:certbot/certbot

apt update
apt-get install certbot
apt install docker-ce -y

curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose

service docker start
docker --version
docker-compose --version

echo "Execute docker-login e depois docker run hello-world para verificar a instalação."
