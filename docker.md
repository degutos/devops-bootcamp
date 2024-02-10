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
$ docker images -q # shows all images id, it doesn't show the header, it is good to use with wc -l
$ docker images -q | wc -l # shows all images id and count how many images id we have
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

# Run container with a blue image tag and map a port

```
$ docker run -p 38282:8080 kodekloud/simple-webapp:blue
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



### Another example of a Docker file

This is only another example of a Dockerfile. This is not part of the project above

```
$ cat Dockerfile 
FROM python:3.6

RUN pip install flask

COPY . /opt/

EXPOSE 8080

WORKDIR /opt

ENTRYPOINT ["python", "app.py"]
```


###  Environment variable

We sometimes want to use variables when we start a container. Some applications all coded with constant set to a value but we can use variables instead 

Example:

```
color = "red" # this is a contstant 

color = os.environ.get('APP_COLOR') # this is a variable
```

We can use the variable set at the container creation time, example:

```
$ docker run -e APP_COLOR=blue simple-webapp-color
```


We can find all the variables set to a container by running 

```
$ docker inspect container_name
...
       "Env": [
                "APP_COLOR=pink",
...
```

Lets see another example of running a container with variables

```
$ docker run -p 38282:8080 --name blue-app -e APP_COLOR=blue -d kodekloud/simple-webapp 
3036928d540e44e14fa84164b4a49c58908a6dc20d0b658dc47c641869bc145e
```

We can confirm the variables with

```
$ docker exec -it blue-app env
PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=3036928d540e
TERM=xterm
APP_COLOR=blue
LANG=C.UTF-8
GPG_KEY=0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D
PYTHON_VERSION=3.6.6
PYTHON_PIP_VERSION=18.1
HOME=/root
```


Creating another container running mysql and setting variable password

```
$ docker run --name mysql-db -d  -e MYSQL_ROOT_PASSWORD=db_pass123   mysql 
f8ab82a707b27567fa24152df79957a1fd1532e0c6cb42843765433dabc791e8
```

Lets check now the variable set

```
$ docker exec -it mysql-db env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=f8ab82a707b2
TERM=xterm
MYSQL_ROOT_PASSWORD=db_pass123
GOSU_VERSION=1.16
MYSQL_MAJOR=8.0
MYSQL_VERSION=8.0.33-1.el8
MYSQL_SHELL_VERSION=8.0.33-1.el8
HOME=/root
```



### Entrypoint vs Command

When we build a container image we can use a variable CMD that will refer to the application which the pod will run 

Example:

```
FROM UBUNTU

CMD sleep 5
```

or 

```
FROM UBUNTU

CMD ['sleep','5']
```

To run the container we can run the below command and we don't pass any parameter and the container will run for 5 seconds

```
docker run ubuntu-sleeper
```

To change the paramenter we will need to inform the command and time, ie.

```
docker run ubuntu-sleeper sleep 10
```

How can we not have to specify the sleep again, ie

```
docker run ubuntu-sleeper 10
```

For the above to work we will need to use ENTRYPOINT

```
FROM UBUNTU
ENTRYPOINT ["sleep"]
CMD ["5"]
```


To modify the entrypoint in runtime 

```
docker run --entrypoint sleep2.0 ubuntu-sleeper 10 
```

### How to run a container with a volume mounted

```
$ docker run -v /opt/data:/var/lib/mysql -d --name mysql-db -e MYSQL_ROOT_PASSWORD=db_pass123 mysql
19240d2384cc1d083047defedabfc5504e703391d1dd7b483c50bb5ce747976a
```


Now we can access the container mysql database and check the content

```
$ docker exec mysql-db mysql -pdb_pass123 -e 'use foo; select * from myTable'
```





## Docker Engine



- Docker CLI
- REST API
- Docker Daemon


#### To access a docker remotely through docker CLI

```
$ docker -H=remote_docker_engine:2375 ...
```

OR

```
$ docker -H=10.123.2.1:2375 run nginx 
```

- Containers are namespaces in the OS separating process in the system.

- We can have PID:1 in the host and another PID:1 within the conatiner.
- This PID:1 has another PID within the OS i.e. PID:5

```
PID:5 in the host == PID:1 in the container namespace, visiable only within the container
```

### CPU and Memory

- By default a container can use all the resources in the host.

- There is a way to restrict resources the container can use

```
$ docker run --cpus=.5 ubuntu
$ docker run --memory=100m ubuntu
```


## File system

- /var/lib/docker 
- /var/lib/docker/volumes
- /var/lib/docker/images


```
$ docker volume create data_volume
```

The above command will create:

- /var/lib/docker/volumes/data_volume

#### Mounting a volume in the container

```
$ docker run -v data_volume:/var/lib/mysql mysql 
```

- If we run -v data_volume2:xxx and data_volume2 doesn't exist the docker engine will create this volume for us.

#### Using mount parameter instead of -v

```
$ docker run \
  --mount type=bind,source=/data/mysql,target=/var/lib/mysql mysql
```


#### lets create another container with mount point volume

```
$ mkdir -p /opt/data

$ docker run -d --name mysql-db -e MYSQL_ROOT_PASSWORD=db_pass123 --mount type=bind,source=/opt/data,target=/var/lib/mysql mysql 
11a3f71dc012aa1af19c26875f5c6dfdfc2b161f532f6f24b3494d7aa3e951f2
```


## Docker Network

- By default docker create a default bridge network on 172.17.0.1 subnet.
- To create another subnet in diffeent range we run

```
$ docker network create \
  --driver bridge \
  --subnet 182.18.0.0/16 \
  custom-isolated-network-andre
```

#### To list all network created

```
$ docker network ls
```

#### How to setup a container and attach it to network none

```
$ docker run -d --name alpine-2 --network none alpine 
c666e505f8699a73afd5974c90f0ed7c1d59fc280fbdf97a541f7dc03d65d2a2
```


#### Create a subnet bridge network 182.18.0.1/24 with gateway 182.18.0.1 named wp-mysql-network

```
$ docker network create --driver bridge --subnet 182.18.0.1/24 --gateway 182.18.0.1 wp-mysql-network
118a051b5c6913250ecd604fc4106f0a26855df4288674ef878787df75936747
$ 
$ docker network ls
NETWORK ID     NAME               DRIVER    SCOPE
5a6507fe6d1a   bridge             bridge    local
e1bd4eeb89ea   host               host      local
cc017d20d8c9   none               null      local
118a051b5c69   wp-mysql-network   bridge    local
```

```
$ docker inspect 118a | egrep -i 'subnet|gateway'
                    "Subnet": "182.18.0.1/24",
                    "Gateway": "182.18.0.1"
```



#### Run a container on specific network

```
$ docker run -d --name mysql-db -e MYSQL_ROOT_PASSWORD=db_pass123 --network wp-mysql-network mysql:5.6
```


#### Run a container exposing a port on the host and set 2 variables and use special subnet created

```
$ docker run -d -p 38080:8080 -e DB_Host=mysql-db -e DB_Password=db_pass123 --network wp-mysql-network --name webapp kodekloud/simple-webapp-mysql 
```


