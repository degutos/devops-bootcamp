# Ansible

## Ansible - beginner


- For this training and module course we are utilize 03 VMs centos:
- ansbile-controller
- ansible-target1
- ansible-target2

- I will personally spin up 03 VSIs in my personal platform cloud gugu to play with ansible


```
[cloud_user@ansible-controller ~]$ hostname
ansible-controller
```

## Installing ansible on controller


```
$ sudo yum install epel-release

$ sudo yum install ansible
```


- In my tests I was not able to install ansible package through the `yum ` on centos8.


```
[cloud_user@ansible-controller ~]$ sudo yum install ansible
Last metadata expiration check: 0:22:46 ago on Sat 02 Mar 2024 16:38:07 UTC.
Error:
 Problem: conflicting requests
  - nothing provides python(abi) = 3.11 needed by ansible-8.3.0-1.el8.noarch
  - nothing provides python3.11dist(ansible-core) >= 2.15.3 needed by ansible-8.3.0-1.el8.noarch
  - nothing provides /usr/bin/python3.11 needed by ansible-8.3.0-1.el8.noarch
(try to add '--skip-broken' to skip uninstallable packages or '--nobest' to use not only best candidate packages)
```

- it seems it is not supported on centos8 as per this git-issue: https://github.com/wazuh/wazuh-ansible/issues/967. Lets try to install Ansible through the pip3


```
[cloud_user@ansible-controller ~]$ pip3 install --upgrade --ignore-installed pip setuptools --user
Collecting pip
  Downloading https://files.pythonhosted.org/packages/a4/6d/6463d49a933f547439d6b5b98b46af8742cc03ae83543e4d7688c2420f8b/pip-21.3.1-py3-none-any.whl (1.7MB)
    100% |████████████████████████████████| 1.7MB 569kB/s
Collecting setuptools
  Downloading https://files.pythonhosted.org/packages/b0/3a/88b210db68e56854d0bcf4b38e165e03be377e13907746f825790f3df5bf/setuptools-59.6.0-py3-none-any.whl (952kB)
    100% |████████████████████████████████| 962kB 1.1MB/s
Installing collected packages: pip, setuptools
Successfully installed pip-21.3.1 setuptools-59.6.0
[cloud_user@ansible-controller ~]$ python3 -m pip install --user ansible
Collecting ansible
  Downloading ansible-4.10.0.tar.gz (36.8 MB)
     |████████████████████████████████| 36.8 MB 18 kB/s
  Preparing metadata (setup.py) ... done
Collecting ansible-core~=2.11.7
  Downloading ansible-core-2.11.12.tar.gz (7.1 MB)
     |████████████████████████████████| 7.1 MB 31.9 MB/s
  Preparing metadata (setup.py) ... done
Requirement already satisfied: jinja2 in /usr/lib/python3.6/site-packages (from ansible-core~=2.11.7->ansible) (2.10.1)
Requirement already satisfied: PyYAML in /usr/lib64/python3.6/site-packages (from ansible-core~=2.11.7->ansible) (3.12)
Requirement already satisfied: cryptography in /usr/lib64/python3.6/site-packages (from ansible-core~=2.11.7->ansible) (3.2.1)
Collecting packaging
  Downloading packaging-21.3-py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB 544 kB/s
Collecting resolvelib<0.6.0,>=0.5.3
  Downloading resolvelib-0.5.4-py2.py3-none-any.whl (12 kB)
Requirement already satisfied: six>=1.4.1 in /usr/lib/python3.6/site-packages (from cryptography->ansible-core~=2.11.7->ansible) (1.11.0)
Requirement already satisfied: cffi!=1.11.3,>=1.8 in /usr/lib64/python3.6/site-packages (from cryptography->ansible-core~=2.11.7->ansible) (1.11.5)
Requirement already satisfied: MarkupSafe>=0.23 in /usr/lib64/python3.6/site-packages (from jinja2->ansible-core~=2.11.7->ansible) (0.23)
Collecting pyparsing!=3.0.5,>=2.0.2
  Downloading pyparsing-3.1.1-py3-none-any.whl (103 kB)
     |████████████████████████████████| 103 kB 45.6 MB/s
Requirement already satisfied: pycparser in /usr/lib/python3.6/site-packages (from cffi!=1.11.3,>=1.8->cryptography->ansible-core~=2.11.7->ansible) (2.14)
Using legacy 'setup.py install' for ansible, since package 'wheel' is not installed.
Using legacy 'setup.py install' for ansible-core, since package 'wheel' is not installed.
Installing collected packages: pyparsing, resolvelib, packaging, ansible-core, ansible
    Running setup.py install for ansible-core ... done
    Running setup.py install for ansible ... done

Successfully installed ansible-4.10.0 ansible-core-2.11.12 packaging-21.3 pyparsing-3.1.1 resolvelib-0.5.4
```


```
[cloud_user@ansible-controller ~]$ ansible --version
[DEPRECATION WARNING]: Ansible will require Python 3.8 or newer on the controller starting with Ansible 2.12. Current version: 3.6.8 (default, Sep 10 2021, 09:13:53) [GCC 8.5.0 20210514 (Red Hat 8.5.0-3)]. This feature will be removed from
ansible-core in version 2.12. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
ansible [core 2.11.12]
  config file = None
  configured module search path = ['/home/cloud_user/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/cloud_user/.local/lib/python3.6/site-packages/ansible
  ansible collection location = /home/cloud_user/.ansible/collections:/usr/share/ansible/collections
  executable location = /home/cloud_user/.local/bin/ansible
  python version = 3.6.8 (default, Sep 10 2021, 09:13:53) [GCC 8.5.0 20210514 (Red Hat 8.5.0-3)]
  jinja version = 2.10.1
  libyaml = True
```

### Connecting to target1 manually to test connectivity 

```
[cloud_user@ansible-controller ~]$ ssh 172.31.106.66
The authenticity of host '172.31.106.66 (172.31.106.66)' can't be established.
ECDSA key fingerprint is SHA256:/f2wkOK5v9LV3eTDpW0LMuCe1Ix2RWvGL35ygQSyYDE.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '172.31.106.66' (ECDSA) to the list of known hosts.
Password:
Activate the web console with: systemctl enable --now cockpit.socket

Last login: Sat Mar  2 16:27:51 2024 from 78.19.34.159
[cloud_user@ansible-target1 ~]$
```

- Once we connect through SSH we can exit from this target1 and go back to ansible-controller

### Inventory file

- Lets create our inventory file in our ansible-controller node

```
[cloud_user@ansible-controller test-project]$ cat > inventory.txt
target1 ansible_host=172.31.106.66 ansible_ssh_pass=my_password_123_REDACTED


[cloud_user@ansible-controller test-project]$ cat inventory.txt
target1 ansible_host=172.31.106.66 ansible_ssh_pass=my_password_123_REDACTED

```

### Ansible ping


- We can use the ansible ad-hoc command and also use the module ping to do our first test
- We can also remove our parameter `ansible_ssh_pass` from our inventory and generate a ssh key in our ansible-controller and copy it over to ansible-target1 machine.

```
[cloud_user@ansible-controller test-project]$ ansible target1 -m ping -i inventory.txt
[DEPRECATION WARNING]: Ansible will require Python 3.8 or newer on the controller starting with Ansible 2.12. Current version: 3.6.8 (default, Sep 10 2021, 09:13:53) [GCC 8.5.0 20210514 (Red Hat 8.5.0-3)]. This feature will be removed from
ansible-core in version 2.12. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
[DEPRECATION WARNING]: Distribution centos 8.5.2111 on host target1 should use /usr/libexec/platform-python, but is using /usr/bin/python for backward compatibility with prior Ansible releases. A future Ansible release will default to using
the discovered platform python for this host. See https://docs.ansible.com/ansible-core/2.11/reference_appendices/interpreter_discovery.html for more information. This feature will be removed in version 2.12. Deprecation warnings can be
disabled by setting deprecation_warnings=False in ansible.cfg.
target1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "ping": "pong"
}
```


- We can also mute the deprecation warning showed above

```
$ export ANSIBLE_DEPRECATION_WARNINGS=False
```

then when we run the ansible ad-hoc command we won't see the warning anymore: 

```
[cloud_user@ansible-controller test-project]$ ansible target1 -m ping -i inventory.txt
target1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "ping": "pong"
}
```

- Lets add the target2 host into our inventory file

```
[cloud_user@ansible-controller test-project]$ cat inventory.txt
target1 ansible_host=172.31.106.66
target2 ansible_host=172.31.111.16
```

- And now we can also test ping module against target2 host:

```
[cloud_user@ansible-controller test-project]$ ansible target2 -m ping -i inventory.txt
target2 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "ping": "pong"
}
```





### Generating our SSH key 

- We can also generate our ssh key in our ansible-controller and send this public key to ansible-target1 machine:

```
[cloud_user@ansible-controller .ssh]$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/cloud_user/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/cloud_user/.ssh/id_rsa.
Your public key has been saved in /home/cloud_user/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:viXVx9pRazJItW9vrQSYb0GjU/fj0xrctviPRZiONEE cloud_user@ansible-controller
The key's randomart image is:
+---[RSA 3072]----+
|            E.   |
|           .. .  |
|           .=.. .|
|          .B.=.=.|
|        S *.*o**o|
|       . . + @*+=|
|        o . = *oO|
|         + . ..Oo|
|        .    .=oo|
+----[SHA256]-----+
```

- Once we generate the key we need to copy the public key to ansible-target1:
  
```
[cloud_user@ansible-controller .ssh]$ ssh-copy-id cloud_user@172.31.106.66
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/cloud_user/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
Password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'cloud_user@172.31.106.66'"
and check to make sure that only the key(s) you wanted were added.
```


### Sample of inventory file

```
web     ansible_host=server1.company.com    ansible_connection=ssh  ansible_user= root  ansible_ssh_pass=Password
db      ansible_host=192.168.0.5            ansible_connection=winrm    ansible_user=admin
localhost                                   ansible_connection=localhost
```

Inventory parameters:

- ansible_connection= ssh/winrm/localhost
- ansible_port= 22/5986
- ansible_user=root/administrator
- ansible_ssh_pass=Password

- Lets see another sample:

```
[bob@student-node playbooks]$ cat inventory 
# Sample Inventory File

web1 ansible_host=server1.company.com
web2 ansible_host=server2.company.com
web3 ansible_host=server3.company.com
db1  ansible_host=server4.company.com
```

- Lets see one more sample, notice we have a windows box and we use the variable `ansible_password` for windows password while we use `ansible_ssh_pass ` for linux machines

```
[bob@student-node playbooks]$ cat inventory 
# Sample Inventory File

# Web Servers
web1 ansible_host=server1.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web2 ansible_host=server2.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web3 ansible_host=server3.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
db1  ansible_host=server4.company.com ansible_connection=winrm ansible_user=administrator ansible_password=Dbp@ss123! 
```

- Lets see another sample with Group web_servers added:

```
[bob@student-node playbooks]$ cat inventory 
# Sample Inventory File

# Web Servers
web1 ansible_host=server1.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web2 ansible_host=server2.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web3 ansible_host=server3.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!

# Database Servers
db1 ansible_host=server4.company.com ansible_connection=winrm ansible_user=administrator ansible_password=Password123!


[web_servers]
web1
web2
web3

[db_servers]
db1
```

- Lets now see another sample with group of groups, where we will have a group called all_servers and within it we will have the other two groups called web_servers and db_servers:

```
[bob@student-node playbooks]$ cat inventory 
# Sample Inventory File

# Web Servers
web1 ansible_host=server1.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web2 ansible_host=server2.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web3 ansible_host=server3.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!

# Database Servers
db1 ansible_host=server4.company.com ansible_connection=winrm ansible_user=administrator ansible_password=Password123!


[web_servers]
web1
web2
web3

[db_servers]
db1

[all_servers:children]
web_servers
db_servers
```

- Now we will see another sample with many group and one group of group:

```
[bob@student-node playbooks]$ cat inventory 
# Sample Inventory File

# Web Servers
web_node1 ansible_host=web01.xyz.com ansible_connection=winrm ansible_user=administrator ansible_password=Win$Pass
web_node2 ansible_host=web02.xyz.com ansible_connection=winrm ansible_user=administrator ansible_password=Win$Pass
web_node3 ansible_host=web03.xyz.com ansible_connection=winrm ansible_user=administrator ansible_password=Win$Pass

# DB Servers
sql_db1 ansible_host=sql01.xyz.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Lin$Pass
sql_db2 ansible_host=sql02.xyz.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Lin$Pass

[db_nodes]
sql_db1
sql_db2

[web_nodes]
web_node1
web_node2
web_node3

[boston_nodes]
sql_db1
web_node1

[dallas_nodes]
sql_db2
web_node2
web_node3

[us_nodes:children]
boston_nodes
dallas_nodes
```


## Playbook samples:

- This example we will execute two commands, the date and cat /etc/resolv with 02 tasks :
  


```
[bob@student-node playbooks]$ cat playbook.yaml 
---
- name: 'Execute two commands on localhost'
  hosts: localhost
  become: yes
  tasks:
    - name: 'Execute a date command'
      command: date       
    - name: 'Task to display nameservers'
      command: cat /etc/resolv.conf
```

- Lets see another sample where we run the same 2 commands but this time against node01:

```
---
- name: 'Execute two commands on node01'
  hosts: node01
  become: yes
  tasks:
    - name: 'Execute a date command'
      command: date
    - name: 'Task to display hosts file'
      command: 'cat /etc/hosts'
```

- Lets see an example now where we run 02 plays, the first play has 2 tasks and second play has only one task

```
[bob@student-node playbooks]$ cat ansible.cfg 
[defaults]
host_key_checking = False
[bob@student-node playbooks]$ cat playbook.yaml 
---
- name: 'Execute two commands on node01'
  hosts: node01
  become: yes
  tasks:
    - name: 'Execute a date command'
      command: date
    - name: 'Task to display hosts file on node01'
      command: 'cat /etc/hosts'
- name: 'Execute a command on node02'
  hosts: node02
  become: yes
  tasks:
          - name: 'Task to display hosts file on node02'
            command: 'cat /etc/hosts'

```

 

## Ansible modules

- System modules: user, group, hostname, iptables, lvg, lvol, mount, systemd
- Command modules: command, script, shell, expect
- File modules: acl, archive, copy, find, replace
- Database modules: mongdb, msql, postgresql, mysql 
- Cloud modules: amazon, azure, DigitalOcean, Openstack, docker, SL, vmware
- Windows modules: win_copy, win_command, win_file
- More...



### Command module

- Lets see an example of command module


```
-
  name: Play1
  hosts: localhost
  tasks: 
    - name: Execute command date
      command: date

    - name: Display resolv.conf contents
      command: cat /etc/resolv.conf 

    - name:  Display resolv.conf contents changing directory
      command: cat resolv.conf chdir=/etc

    - name: Display resolv.conf contents
      command: mkdir /folder creates=folder

    - name: Copy file from source to destination
      copy: src=/source_file dest=/destination
```



### Script module

- Script module run a local script on a remote node after transfering it

```
- 
  name: Play2
  hosts: localhost
  tasks:
    - name: Run script on a remote server
      script: /some/local/script.sh -arg1 -arg2
```

### Service modules

- Service module is to manage services on a node like start, stop, restart

```
- 
  name: Start Services in order
  hosts: localhost
  tasks: 
    - name: Start database service
      service: name=postgresql state=started
```

Another way of right the same thing

```
...
tasks:
  - name: Start database service
    service:
      name: postgresql
      state: started
```

- Lets now add 02 more tasks to the first example above:


```
- 
  name: Start Services in order
  hosts: localhost
  tasks: 
    - name: Start database service
      service: name=postgresql state=started
    - name: Start httpd service
      service: name=httpd state=started
    - name: Start nginx service
      service: name=nginx state=started
```


- Keep in mind that we are instructing ansible to make sure the service is `started` we are not asking ansible to start. If the service is started the ansible will do nothing since the service is already started.


### Lineinfile module


```
- 
  name: Add DNS server to resolv.conf
  hosts: localhost
  tasks:
    - lineinfile:
        path: /etc/resolv.conf
        line: 'nameserver 10.1.250.10' 
```



### Example of playbook to create a file /var/www/html/index.html and add a line "Welcome... " to it

```
[bob@student-node playbooks]$ cat playbook.yaml 
---
- name: 'hosts'
  hosts: all
  become: yes
  tasks:
    - name: 'Execute a script'
      script: '/tmp/install_script.sh'    
    - name: 'Start httpd service'
      service:
        name: 'httpd'
        state: 'started'
    - lineinfile:
        path: /var/www/html/index.html
        line: 'Welcome to ansible-beginning course' 
        create: true

```

### Example of playbook to create a user with uid 1040 and group developer

```
[bob@student-node playbooks]$ cat playbook.yaml 
---
- name: 'hosts'
  hosts: all
  become: yes
  tasks:
    - name: 'Execute a script'
      script: '/tmp/install_script.sh'
    - name: 'Start httpd service'
      service:
        name: 'httpd'
        state: 'started'
    - name: "Update /var/www/html/index.html"
      lineinfile:
        path: /var/www/html/index.html
        line: "Welcome to ansible-beginning course"
        create: true
    - name: Create user
      user:
              name: web_user
              uid: 1040
              group: developers

```

### Variables

- We can also use variables to work with anisble



```
- 
  name: Add DNS server to resolv.conf
  hosts: localhost
  vars:
    dns_server: 10.1.250.10
  tasks:
    - lineinfile:
        path: /etc/resolv.conf
        line: 'nameserver {{ dns_server }}'


- We can also have a separated file to store our variables

variables
```
variable1: value1
variable2: value2
```


- Lets see another example with many variables in the playbook:


```
- 
  name: Set firewall config
  hosts: web
  tasks:
    - firewalld:
      service: htpps
      permanent: true
      state: enabled

    - firewalld:
      port: '{{ httpd_port }}'/tcp
      permanent: true
      state: disabled

    - firewalld:
      port: '{{ snmp_port }}'/udp
      permanent: true
      state: disabled 

    - firewalld:
      source: '{{ inter_ip_range }}'/24
      zone: internal
      state: enabled
```


- lets now create our web.yml file

```
http_port: 8081
snmp_port: 161-162
inter_ip_range: 192.0.2.0
```



### Example using variables

```
[bob@student-node playbooks]$ cat playbook.yaml 
---
- name: 'Add nameserver in resolv.conf file on localhost'
  hosts: localhost
  become: yes
  tasks:
    - name: 'Add nameserver in resolv.conf file'
      lineinfile:
        path: /tmp/resolv.conf
        line: 'nameserver {{ nameserver_ip }}' 
```

- Variables in this example are added to inventory file:

```
[bob@student-node playbooks]$ cat inventory 
localhost ansible_connection=local nameserver_ip=8.8.8.8 snmp_port=160-161
node01 ansible_host=node01 ansible_ssh_pass=caleston123
node02 ansible_host=node02 ansible_ssh_pass=caleston123
[web_nodes]
node01
node02

[all:vars]
app_list=['vim', 'sqlite', 'jq']
user_details={'username': 'admin', 'password': 'secret_pass', 'email': 'admin@example.com'}
```

- Another example below, notice that the variable nameserver_ip is set in the above file inventory:

```
[bob@student-node playbooks]$ cat playbook.yaml 
---
- name: 'Add nameserver in resolv.conf file on localhost'
  hosts: localhost
  become: yes
  tasks:
    - name: 'Add nameserver in resolv.conf file'
      lineinfile:
        path: /tmp/resolv.conf
        line: 'nameserver {{  nameserver_ip  }}'
    - name: 'Disable SNMP Port'
      firewalld:
        port: '{{ snmp_port }}' 
        permanent: true
        state: disabled 
```


  
- Anather example:

```
[bob@student-node playbooks]$ cat playbook.yaml 
---
- hosts: localhost
  vars:
    car_model: 'BMW M3'
    country_name: USA
    title: 'Systems Engineer' 

  tasks:
    - command: 'echo "My car is {{ car_model }}"'
    - command: 'echo "I live in {{ country_name }}"'
    - command: 'echo "I work as a {{ title }}"'
  ```


  - Lets see another exmaple with several items to be installed:

  ```
  [bob@student-node playbooks]$ cat app_install.yaml 
---
- hosts: all
  become: yes
  tasks:
    - name: Install applications
      yum:
        name: "{{ item }}"
        state: present
      with_items:
        - "{{ app_list }}" 
  ```

  - Lets see now our variables file 

  ```
  [bob@student-node playbooks]$ cat inventory 
localhost ansible_connection=local nameserver_ip=8.8.8.8 snmp_port=160-161
node01 ansible_host=node01 ansible_ssh_pass=caleston123
node02 ansible_host=node02 ansible_ssh_pass=caleston123
[web_nodes]
node01
node02

[all:vars]
app_list=['vim', 'sqlite', 'jq']
user_details={'username': 'admin', 'password': 'secret_pass', 'email': 'admin@example.com'}
```

- One more example to create user with variables:

```
[bob@student-node playbooks]$ cat user_setup.yaml 
---
- hosts: all
  become: yes
  tasks:
    - name: Set up user
      user:
        name: "{{ user_details.username }}"
        password: "{{ user_details.password }}"
        comment: "{{ user_details.email }}" 
        state: present
```

- Lets check now the variables file:

```
[bob@student-node playbooks]$ cat inventory 
localhost ansible_connection=local nameserver_ip=8.8.8.8 snmp_port=160-161
node01 ansible_host=node01 ansible_ssh_pass=caleston123
node02 ansible_host=node02 ansible_ssh_pass=caleston123
[web_nodes]
node01
node02

[all:vars]
app_list=['vim', 'sqlite', 'jq']
user_details={'username': 'admin', 'password': 'secret_pass', 'email': 'admin@example.com'}
```










LAB

In this lab exercise you will use below hosts. Please note down some details about these hosts as given below :


student-node :- This host will act as an Ansible master node where you will create playbooks, inventory, roles etc and you will be running your playbooks from this host itself.


node01 :- This host will act as an Ansible client/remote host where you will setup/install some stuff using Ansible playbooks. Below are the SSH credentials for this host:


User: bob
Password: caleston123


node02 :- This host will also act as an Ansible client/remote host where you will setup/install some stuff using Ansible playbooks. Below are the SSH credentials for this host:


User: bob
Password: caleston123


Note: Please type exit or logout on the terminal or press CTRL + d to log out from a specific node.




