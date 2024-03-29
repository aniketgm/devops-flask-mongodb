# Simple Flask Login App using MongoDB
This repo contains a simple flask app that uses the Mongo Database to store user data. This app will be build, tested and deployed. Where it will be deployed ? I'm still working on that.

The code in this repo, is build upon the tutorial code by Luke Peters: [Github Tutorial Page](https://github.com/LukePeters/User-Login-System-Tutorial).
I've modified the code and added some test so as to use this app for building a CI/CD pipeline.
Although test were not really required for learning CI/CD. However, it is expected that any application must have a tests when deploying some application. So as a norm, I wrote some tests for the App.

## Features
The Flask MongoDB app mainly has two features:

### Signup
Here,
* The user sign's up into the app.
* The details provided into the form presented to the user is stored into the mongo db.
* A Dashboard page is presented to the user after successful signup.
* When user sign' out. the home page is displayed again.

### Login
Here,
* The user provides only email and password into the form.
* These details are verified with the DB values and once successful, the user is presented with the Dashboard page
* Home page is displayed on signout.

## About the test
The app is tested using the [unittest](https://docs.python.org/3/library/unittest.html) framework that comes built-in any python installation.

## Docker configuration
* The [Dockerfile](https://github.com/aniketgm/devops-flask-mongodb/blob/main/Dockerfile) contains the code to create a docker image containing Jenkins and Python.

* With this Dockerfile, we first build the file, which will create a docker image as follows:
```
$ docker build -t jenkins-python:test .
```

* I've given the name here as /jenkins-python/. However, any name can be given for the image. After the image is created, the following command will create a container with some random name unless a <CONTAINER_NAME> is specified.
```
$ docker run -p 8080:8080 jenkins-python:test --name <CONTAINER_NAME>
```
