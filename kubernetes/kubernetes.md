# Kubernetes

## Overview

- Understand container
- Understand orchestration 

### Containers Overview

- We will need a container engine like containerd for example
- Isolate process, Network and mount point
- They all share the same kernel 
- Containers are not virtual machine
- Images are meant to create containers


### Container orchestration 

- We need an orchestration to manage different pods running in different nodes. 
- Kubernetes is one of the orchestration tool availabile today
- We can have also docker swarm and mesos as orchestration 
  


### Kube architecture 

- Nodes or worker nodes
- We need more than one node in our cluster
- We need a control plane, master

#### Main resources in the kubernetes 

- API server
- ETCD
- kubelet
- Container runtime
- Controller
- Scheduler 
  
### Kubectl 

```
➜  ~ k run nginx --image nginx
pod/nginx created
```

```
➜  ~ k get pods
NAME    READY   STATUS    RESTARTS   AGE
nginx   1/1     Running   0          54s
```

#### Describe Pods


```
➜  ~ k get po -o wide
NAME    READY   STATUS    RESTARTS   AGE     IP           NODE                 NOMINATED NODE   READINESS GATES
nginx   1/1     Running   0          7m57s   10.244.0.7   kind-control-plane   <none>           <none>
```


```
➜  ~ k describe po nginx
Name:             nginx
Namespace:        default
Priority:         0
Service Account:  default
Node:             kind-control-plane/172.18.0.2
Start Time:       Sat, 10 Feb 2024 17:35:25 +0000
Labels:           run=nginx
Annotations:      <none>
Status:           Running
IP:               10.244.0.7
IPs:
  IP:  10.244.0.7
Containers:
  nginx:
    Container ID:   containerd://ff28784c0bdb63fcaa235cdd334e481ff26a25c1c850f26ba82f59c004763b29
    Image:          nginx
    Image ID:       docker.io/library/nginx@sha256:84c52dfd55c467e12ef85cad6a252c0990564f03c4850799bf41dd738738691f
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Sat, 10 Feb 2024 17:35:26 +0000
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-w66mb (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True
  Initialized                 True
  Ready                       True
  ContainersReady             True
  PodScheduled                True
Volumes:
  kube-api-access-w66mb:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  6m18s  default-scheduler  Successfully assigned default/nginx to kind-control-plane
  Normal  Pulling    6m18s  kubelet            Pulling image "nginx"
  Normal  Pulled     6m17s  kubelet            Successfully pulled image "nginx" in 862ms (862ms including waiting)
  Normal  Created    6m17s  kubelet            Created container nginx
  Normal  Started    6m17s  kubelet            Started container nginx
➜  ~
```




#### Deployment

```
➜  ~ k create deployment hello-andre --image=nginx
deployment.apps/hello-andre created
```

```
➜  ~ kubectl get deploy
NAME          READY   UP-TO-DATE   AVAILABLE   AGE
hello-andre   1/1     1            1           7s
```

```
➜  ~ kubectl get po
NAME                          READY   STATUS    RESTARTS   AGE
hello-andre-c6bbbb466-rd4dl   1/1     Running   0          14s
```


