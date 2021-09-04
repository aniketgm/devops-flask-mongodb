FROM jenkins/jenkins:lts
USER root
RUN mkdir /flask-mdb-app
WORKDIR /flask-mdb-app
COPY . /flask-mdb-app
RUN rm -fv Dockerfile README.org
RUN apt-get update
RUN apt-get install -y python3
