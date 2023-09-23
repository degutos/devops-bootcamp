# Jenkins

## Introduction

## Aplication introduction

#### Cloning an application

```
[bob@centos-host ~]$ git clone https://github.com/kodekloudhub/go-webapp-sample
Cloning into 'go-webapp-sample'...
remote: Enumerating objects: 1660, done.
remote: Counting objects: 100% (518/518), done.
remote: Compressing objects: 100% (60/60), done.
remote: Total 1660 (delta 478), reused 458 (delta 458), pack-reused 1142
Receiving objects: 100% (1660/1660), 20.76 MiB | 26.15 MiB/s, done.
Resolving deltas: 100% (996/996), done.
```


#### Running a Go application

```
[bob@centos-host go-webapp-sample]$ go run main.go 
go: downloading github.com/labstack/echo/v4 v4.6.3
go: downloading gorm.io/driver/postgres v1.2.3
go: downloading gorm.io/driver/sqlite v1.2.6
go: downloading github.com/labstack/echo-contrib v0.11.0
go: downloading gorm.io/gorm v1.22.5
go: downloading github.com/jinzhu/configor v1.2.1
go: downloading gorm.io/driver/mysql v1.2.3
go: downloading gopkg.in/boj/redistore.v1 v1.0.0-20160128113310-fc113767cd6b
go: downloading github.com/gorilla/sessions v1.2.1
go: downloading go.uber.org/zap v1.20.0
...
2023-09-15T10:40:56.085Z        DEBUG   logger/gormlogger.go:58 [gorm] INSERT INTO `format_master` (`name`) VALUES ("Paper Book")
2023-09-15T10:40:56.088Z        DEBUG   logger/gormlogger.go:58 [gorm] INSERT INTO `format_master` (`name`) VALUES ("e-Book")
2023-09-15T10:40:56.152Z        INFO    go-webapp-sample/main.go:42     Served the static contents. path: ./

public/

   ____    __
  / __/___/ /  ___
 / _// __/ _ \/ _ \
/___/\__/_//_/\___/ v4.6.3
High performance, minimalist Go web framework
https://echo.labstack.com
____________________________________O/_______
                                    O\
⇨ http server started on [::]:8090
```




# CI / CD - Continuos Integration and Continuos Delivery 

## CI

CI is the process to test your code, unit test and integration test, all dependencies are satisfyied, all the security checks are run on your code, is also the place where you package your code and leave it ready to deploy.


## CD - Continous delivery or continuos deployment

Once the package is done your will need get package and deploy it in the environment.


 