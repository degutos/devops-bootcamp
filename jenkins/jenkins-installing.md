# Jenkins

## Installation 

We will need to install java package as a pre-requisite to install jenkins

```
$ sudo yum install epel-release -y
$ sudo yum install java-11-openjdk -y
$ sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo --no-check-certificate
$ sudo rpm --import http://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
$ sudo yum install jenkins -y
```


Note:

Edit `/lib/systemd/system/jenkins.service` file and change Jenkins port to 8090 if you wish by updating Environment="JENKINS_PORT=" variable value, otherwise let it as default.

```
sudo vi /lib/systemd/system/jenkins.service
```

```
sudo systemctl start jenkins
```


### Configuruing a ssh key in jenkins

We can setup a public ssh key in order to access the jenkins server through the UI
After adding our key we are ready to reach the jenkins api through the curl command

```
curl -Lv http://localhost:8085/login 2>&1 | grep -i 'x-ssh-endpoint'

```


Example:

```
$ curl -Lv http://localhost:8085/login 2>&1 | grep -i 'x-ssh-endpoint'
< X-SSH-Endpoint: 8085-port-362eceb46b2446ba.labs.kodekloud.com:8022
```

As we see this server is using the port 8085 for login and 8022 for the application


### Interacting with jenkins server through the CLI

```
$ ssh -i /home/mike/.ssh/jenkins_key -l mike -p 8022 jenkins-server help
```

