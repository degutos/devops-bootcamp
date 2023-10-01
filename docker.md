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
$ docker ps # shows running container
$ docker ps -a # shows all container running and stopped 
$ docker stop silly_sammet # stop a container
$ docker rm silly_sammet # remove a container forever
$ docker images # shows all images we have downloaded
$ docker rmi image_name # delete an image 
$ docker run nginx # run and download an image
$ docker pull image # download an image
$ docker run ubuntu sleep 15 # run container ubuntu and runs sleep for 15 seconds
$ docker exec distracted_rock cat /etc/hosts # exec a command within a container
$ docker attach container_id # connect/attach to a container 
$ docker run -d ubuntu # run container in daemon mode 
```


