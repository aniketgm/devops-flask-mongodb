FROM jenkins/jenkins:lts
USER root
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y git
