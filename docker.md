 # Docker

## Docker versions

- Docker Community Edition 
- Docker enterprise Edition

## Setup and Installation 

- Go to docs.docker.com and get docker
- Uninstall any existing old docker version 
- Install the pre-requisites and docker 

```
$ sudo yum remove docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras
```

- Installing 

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
```

## Running a test container 

```
➜  ~ docker run docker/whalesay cowsay Love-You!
Unable to find image 'docker/whalesay:latest' locally
latest: Pulling from docker/whalesay
[DEPRECATION NOTICE] Docker Image Format v1, and Docker Image manifest version 2, schema 1 support will be removed in an upcoming release. Suggest the author of docker.io/docker/whalesay:latest to upgrade the image to the OCI Format, or Docker Image manifest v2, schema 2. More information at https://docs.docker.com/go/deprecated-image-specs/
e190868d63f8: Pull complete
909cd34c6fd7: Pull complete
0b9bfabab7c1: Pull complete
a3ed95caeb02: Pull complete
00bf65475aba: Pull complete
c57b6bcc83e3: Pull complete
8978f6879e2f: Pull complete
8eed3712d2cf: Pull complete
Digest: sha256:178598e51a26abbc958b8a2e48825c90bc22e641de3d31e18aaf55f3258ba93b
Status: Downloaded newer image for docker/whalesay:latest
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested
 ___________
< Love-You! >
 -----------
    \
     \
      \
                    ##        .
              ## ## ##       ==
           ## ## ## ##      ===
       /""""""""""""""""___/ ===
  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~
       \______ o          __/
        \    \        __/
          \____\______/
```

## Docker commands


```
$ docker -v # check docker engine version 
$ docker ps # shows running container
$ docker ps -a # shows all container running and stopped 
$ docker stop silly_sammet # stop a container
$ docker rm silly_sammet # remove a container forever
$ docker images # shows all images we have downloaded
$ docker rmi image_name # delete an image 
$ docker run nginx # run and download an image
$ docker pull image # download an image
$ docker run ubuntu sleep 15 # run container ubuntu and runs sleep for 15 seconds
$ docker exec distracted_rock cat /etc/hosts # exec a command within a running container
$ docker attach container_id # connect/attach to a container 
$ docker run -d ubuntu # run container in daemon mode 
$ docker run -it centos bash # run a container centos in interactive mode using bash console
$ docker rmi $(docker images -q) # remove all images
$ docker rm $(docker ps -a -q) # remove all containers
$ docker pull nginx:1.14-alpine # pull an image 
```

```
$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
3cfb24e9d24c   alpine         "sleep 1000"             About a minute ago   Up About a minute             sad_banzai
4b35261bad8c   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    nginx-2
8827d8811ed6   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    nginx-1
e61157d7b44c   ubuntu         "sleep 1000"             About a minute ago   Up About a minute             awesome_northcut
```

# Run a container and map a port into the node

```
$ docker run -p 80:8080 nginx # run a container and map a port 80 on the worker node to port 8080 on the container
```


# Run container and map volume

```
$ docker run -v /opt/datadir:/var/lib/mysql mysql 
```

# docker inspect and docker logs

```
$ docker inspect containerid
$ docker logs container_id
```

 # Installing a Jenkins container

 ```
 $ docker run -p 8080:8080 -v /home/user/jenkins-data:/var/jenkins_home -u user jenkins
 ```



 # Docker Images

 ### Containarizing a flask web application


#### How to create my own image 


1. OS - Ubuntu
2. Update apt repo
3. Install dependencies using apt
4. Install python dependencies using pip
5. Copy source code to /opt folder
6. Run the web server using flask command


##### Dockerfile

Create your Dockerfile

```
FROM ubuntu

RUN apt-get update
RUN apt-get install python

RUN pip install flask
RUN pip install flask-mysql

COPU . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run

```


##### Build docker image

```
$ docker build Dockerfile -t mmumshad/my-custom-app
$ docker push mmumshad/my-custom-app
```

##### Docker layer

There will be different layers in our container accordingly to our commands added to the Dockerfile

- Layer 1 - Base ubuntu layer
- Layer 2 - Changes in apt packages
- Layer 3 - Changes in pip packages
- Layer 4 - Source code
- Layer 5 - Update Entrypoint with flask command


##### Docker history command

With docker history we can see the layers we built our container and the size of each layer.

```
$ docker history mumshad/single-webapp
```

## Docker image project - hands on


We will be deploying an application test from https://github.com/mmumshad/simple-webapp-flask/tree/master


### Running Flask application manually in the ubuntu container

```
$ docker run -it -p 8080:8080  ubuntu  bash
$ apt-get update
$ apt-get install -y python2 pip
$ pip install flask
$ cat > /opt/app.py
import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
CTRL+C


$  FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
```


Now you open your browser!

```
* Running on http://127.0.0.1:8080
* Running on http://localhost:8080
```

# Lets dockerize our application 


### Create a dir to build your new container

```
$ mkdir my-simple-webapp
```

```
$ cd my-simple-webapp 
```

## Create your Dockerfile

```
$ cat > Dockerfile   
FROM ubuntu

RUN apt-get update
RUN apt-get install -y python2 pip
RUN pip install flask 

COPY app.py /opt/app.py
    
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
^C
```

### Create your app.py within your Project dir with your Dockerfile

```
$ cat > app.py    
import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
^C
```

### Create your container and tag it 

```
$ docker build . -t degutos/my-simple-webapp
```

You will be able to see you image created

```
$ docker images                             
REPOSITORY                    TAG         IMAGE ID       CREATED              SIZE
degutos/my-simple-webapp      latest      d05ba7edf9b5   About a minute ago   480MB
```


### Running our container recently created

```
$ docker run -p 8080:8080 degutos/my-simple-webapp
```

After that we will be able to open our browser on port 8080

```
* Running on http://127.0.0.1:8080
* Running on http://localhost:8080
```


### Pushing our image to docker hub


```
$ docker login            
Authenticating with existing credentials...
Login Succeeded
```

```
$ docker push degutos/my-simple-webapp
Using default tag: latest
The push refers to repository [docker.io/degutos/my-simple-webapp]
af93081ec0de: Pushed 
fd187973b88b: Pushed 
b93b63bf3160: Pushed 
ca2650d3319c: Pushed 
94360412eb96: Mounted from library/ubuntu 
latest: digest: sha256:09a373618d2a613a9dbfcdc3db74147770a3c0b020cf803eaa1f5e2509854b04 size: 1372
```





