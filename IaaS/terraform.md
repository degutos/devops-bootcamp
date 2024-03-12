# IAAS - Infrastructure as a Service

- We can write code to manage our infrastructure, this is called infrastructure as a code
  

## Types of IAC tools


- Configuration Management 
  - Ansible
  - Chef 
  - puppet 
  - Saltstack 
- Server templating
  - docker
  - packer
  - vagrant 
- Provisioning tools
  - Terraform
  - CloudFormation
  
### Configuration Management

- Designed to install and manage software
- maintains standard structure 
- version control
- idempotent (run the code multiple times it only changes when needed)

### Server templating tools

- Pre installed software and dependencies 
- Virtual machine or docker images
- immutable infrastructure 

### Provisioning tools

- Deploy immutable infrastructure resources
- Servers, databases, network components etc
- multiple providers
  

## Why Terraform 

- Provision physical machines
- Vmware 
- AWS
- GCP
- Azure
- etc
- BipIP
- CloudFlare
- DNS
- Grafana
- MongoDB
- Mysql
- Postgresql 
- Kubernetes

- Quickly to deploy and can be destroy if need
- Can have state of our Infra
- HCL - Hashicorp configuration language
- Easy to understand language 
- easy to share our code
- Code is declarative we declare the desire state. 


### Main commands

- terraform init
- terraform plan
- terraform apply

- Terraform has a file with the current state called terraform.tfstate 


## Terraform installation 

- Terraform is supported on linux, mac, windows, openbsd, solaris, freebsd etc
  

```
$ wget https://releases.hashicorp.com/terraform/0.13.0/terraform_0.13.0_linux_amd64.zip
$ unzip terraform_0.13.0_linux_amd64.zip
$ mv terraform /usr/local/bin/
$ terraform version
  Terraform v0.13.0
```

## HCL Declarative language

aws.tf
```
resource "aws_instance" "webserver" {
  ami = "ami-0c2f25c1f66"
  instance_type = "t2.micro"
}
```
- Resource is a object that terraform manages, it could be resources like  a file, virtual machine, ec2, bucket, roles, policies, compute engine, database, etc.

Syntaxe:

```
<block> <parameters> {
  key1 = value1
  key2 = value2
}
```

### Create a local file

local.tf
```
resource "local_file" "pet" {
  filename = "/root/pets.txt"
  content = "We love pets!"
}
```

### Samples of terraform 

aws-ec2.tf
```
resource "aws_instance" "webserver" {
  ami = "ami-0c2f25d1f66"
  instance_type = "t2.micro"
}
```

aws-s3.tf
```
resource "aws_s3_bucket"  "data" {
  bucket = "webserver-bucket-org-2207"
  acl = "private"
}
```

- terraform init
- terraform plan
- terraform apply
- terraform show -> will show detail resources 

To use terraform local_file resource we can refer to documentation page:
https://registry.terraform.io/providers/hashicorp/local/latest/docs/resources/file

```
resource "aws_instance" "dev-server" {
    instance_type = "t2.micro"
    ami         = "ami-02cff456777cd"
}
resource "aws_s3_bucket" "falshpoint"  {
    bucket = "project-flashpoint-paradox"
}
```

### Creating our first terraform script

```
resource "local_file" "pet" {
    filename = "./pets.txt"
    content = "We love pets!"
    file_permission = "0700"
```

```
➜  tf-samples git:(main) ✗ terraform init 

Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/local...
- Installing hashicorp/local v2.4.1...
- Installed hashicorp/local v2.4.1 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

```
➜  tf-samples git:(main) ✗ terraform plan 

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # local_file.pet will be created
  + resource "local_file" "pet" {
      + content              = "We love pets!"
      + content_base64sha256 = (known after apply)
      + content_base64sha512 = (known after apply)
      + content_md5          = (known after apply)
      + content_sha1         = (known after apply)
      + content_sha256       = (known after apply)
      + content_sha512       = (known after apply)
      + directory_permission = "0777"
      + file_permission      = "0777"
      + filename             = "./pets.txt"
      + id                   = (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
```

```
$ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # local_file.pet will be created
  + resource "local_file" "pet" {
      + content              = "We love pets!"
      + content_base64sha256 = (known after apply)
      + content_base64sha512 = (known after apply)
      + content_md5          = (known after apply)
      + content_sha1         = (known after apply)
      + content_sha256       = (known after apply)
      + content_sha512       = (known after apply)
      + directory_permission = "0777"
      + file_permission      = "0777"
      + filename             = "./pets.txt"
      + id                   = (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

local_file.pet: Creating...
local_file.pet: Creation complete after 0s [id=cba595b7d9f94ba1107a46f3f731912d95fb3d2c]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

- Lets what resource it created

```
➜  tf-samples git:(main) ✗ ls -lh 
total 32
-rw-r--r--  1 degutos  staff   118B Mar  8 13:18 local.tf
-rwx------  1 degutos  staff    13B Mar  8 13:19 pets.txt
-rw-r--r--  1 degutos  staff   1.4K Mar  8 13:19 terraform.tfstate
-rw-r--r--  1 degutos  staff   1.4K Mar  8 13:19 terraform.tfstate.backup
```

- Lets destroy our resource 

```
$ terraform destroy
local_file.pet: Refreshing state... [id=cba595b7d9f94ba1107a46f3f731912d95fb3d2c]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # local_file.pet will be destroyed
  - resource "local_file" "pet" {
      - content              = "We love pets!" -> null
      - content_base64sha256 = "zUA5Ip/IeKlmTQIptlp90JdMGAd8YLStDXhpGq0Bp0c=" -> null
      - content_base64sha512 = "tduqTz5S8Wa3O9Ab5+g0GcGL6kMjMh61vjFcMm5KkOO5TgViAC/kBOdvYHl9qky2K99+u80z0CfCs2ExsHbjGg==" -> null
      - content_md5          = "f510a471c5dc0bcd4759ad9dc81a516f" -> null
      - content_sha1         = "cba595b7d9f94ba1107a46f3f731912d95fb3d2c" -> null
      - content_sha256       = "cd4039229fc878a9664d0229b65a7dd0974c18077c60b4ad0d78691aad01a747" -> null
      - content_sha512       = "b5dbaa4f3e52f166b73bd01be7e83419c18bea4323321eb5be315c326e4a90e3b94e0562002fe404e76f60797daa4cb62bdf7ebbcd33d027c2b36131b076e31a" -> null
      - directory_permission = "0777" -> null
      - file_permission      = "0700" -> null
      - filename             = "./pets.txt" -> null
      - id                   = "cba595b7d9f94ba1107a46f3f731912d95fb3d2c" -> null
    }

Plan: 0 to add, 0 to change, 1 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

local_file.pet: Destroying... [id=cba595b7d9f94ba1107a46f3f731912d95fb3d2c]
local_file.pet: Destruction complete after 0s

Destroy complete! Resources: 1 destroyed.
```


- We can also create a file with sensitive content, this will not show on the screen during terraform plan and terraform apply

```
resource "local_sensitive_file" "foo" {
  content  = "foo!"
  filename = "/root/foo.bar"
}
```

## Terraform Providers


- When we run `terraform init` on a directory with HCL file like `local.tf` the terraform will download a provider plugin like aws,gcp or local provider that we created a local file on local computer.
- We can have official provider, verified provider, community providers
- We can have multiples different providers. For example random provider, with this provider we can use random_id, random_integer, random_password, random_pet, random_string, random_uuid, etc

Example:

```
resource "random_pet" "my-pet" {
  prefix = "Mrs"
  separator = "."
  length = "1"
}
```

```
resource "kubernetes_namespace" "dev" {
  metadata {
    name = "development"
  }
}
```

```
resource "aws_instance" "ec2_instance" {
	  ami       =  "ami-0eda277a0b884c5ab" 
	  instance_type = "t2.large"
}


resource "aws_ebs_volume" "ec2_volume" {
	  availability_zone = "eu-west-1"
	  size  =    10
}
```

```
resource "local_file" "iac_code" {
	  filename = "/opt/practice"
	  content = "Setting up infrastructure as code"
}


resource "random_string" "iac_random" {
  length = 10
  min_upper = 5
}

```


## Variables

variables.tf

```
variable "filename" {
  default = "/root/pets.txt"
}

variable "content" {
  default = "We love pets!"
}

variable "prefix" {
  default = "Mrs"
}

variable "separator" {
  default = "."
}

variable "length" {
  default = "1"
}
```

main.tf

```
resource "local_file" "pet" {
  filename = var.filename
  content = var.content
}

resource "random_pet" "my-pet" {
  prefix = var.prefix
  separator = var.separator
  length = var. length
}
```

- When we use variables and if we need to change anything we can change in variables.tf file and not in main.tf
- We can have more properties to variables.tf file, example:

variables.tf
```
variable "length" {
  default = 2
  type = number
  description = "length of the pet name"
}

variable "password_change" {
  default = true
  type = bool
}
```

### type of variables

- string = "/root/pets.txt"
- number = 1
- bool = true/false
- any = Default value
- list = ["cat","dog"]
- map = pet1 = cat
        pet2 = dog
- object = complex data structure
- tuple = complex data structure 

#### List

variables.tf
```
variable "prefix" {
  default = ["Mr","Mrs","Sir"]
  type = list # 0   1     2
}
```

main.tf
```
resource "random_pet" "my-pet" {
  prefix = var.prefix[0]
}
```

#### Map

variables.tf
```
variable file-content {
  type = map
  default = {
    "statement1" = "We love pets!"
    "statement2" = "We love animals!"
  }
}
```

main.tf
```
resource "local_file" "my-pet" {
  filename = "/root/pets.txt"
  content = var.file-content["statement2"]
}
```

#### List of types

```
variable "prefix" {
  default = ["Mr","Mrs", "Sir"]
  type = list(string)
}
```

#### Map of a type

```
variables "cats" {
  default = {
    "color" = "brown"
    "name" = "bella"
  }
  type = map(string)
}
```

#### Set

- Set is like a List but set doesn't accept duplicated variables value

```
variable "prefix" {
  default = ["Mr","Mrs","Sir"]
  type = set(string)
}
```

- Set doesn't accept duplicated 

```
variable "prefix" {
  default = ["Mr","Mrs","Sir","Sir"]
  type = set(string)
}
```

- The above example will FAIL when we run terraform apply


#### Object

```
variable "bella" {
  type = object({
    name = string
    color = string
    age = number
    food = list(string)
    favorite_pet = bool
  })
  default = {
    name = "bella"
    color = "brown"
    age = 7
    food = ["fish","chicken","turkey"]
    favorite_pet = true
  }
}
```

#### Tuples

```
variable "kitty" {
  type = tuple([string,number, bool])
  default = ["cat",7,true]
}
```


#### Example of variables

```
variable "name" {
     type = string
     default = "Mark"
  
}
variable "number" {
     type = bool
     default = true
  
}
variable "distance" {
     type = number
     default = 5
  
}
variable "jedi" {
     type = map
     default = {
     filename = "/root/first-jedi"
     content = "phanius"
     }
  
}

variable "gender" {
     type = list(string)
     default = ["Male", "Female"]
     }
variable "hard_drive" {
     type = map
     default = {
          slow = "HHD"
          fast = "SSD"
     }
}
variable "users" {
     type = set(string)
     default = ["tom", "jerry", "pluto", "daffy", "donald", "jerry", "chip", "dale"]
}
```

```
resource "local_file" "jedi" {
     filename = var.jedi.filename
     content = var.jedi.content
}

```

#### Terraform variables in execution time or setting variable with export 

- We can also pass the variables names and values during the CLI, example:

```
$ terraform apply -var "filename=/root/pets.txt" -var "content=We love Pets!" -var "prefix=Mrs" -var "separator=." -var "length=2"
```

- If we don't pass any parameter and our variables.tf file has not the variable default value the terraform will prompt you during the execution time 
- We can also export variables, example:

```
export TF_VAR_filename="/root/pets.txt"
export TF_VAR_content="We love pets!"
export TF_VAR_prefix="Mrs"
export TF_VAR_separator="."
export TF_VAR_length="2"
$ terraform apply 
```

- We can aso create a file terraform.tfvars to set up all our variables

terraform.tfvars
```
filename = "/root/pets.txt"
content = "We love pets!"
```

OR we can call a different name file in command line, example:

```
$ terraform apply -var-file variables.tfvars
```

- Order of variables places 

- 1st: Environment variables - export TF_VAR_
- 2st: terraform.tfvars
- 3rd: *auto.tfvars 
- 4th: -var or -var-file (command-line flags)

- The last one above is the preferable way which means it will run the -var or -var-file value passed




#### Variables to create an AWS resource

variables.tf
```
variable "ami" {
  default = "ami=03dab43b6"
}

variable "instance_type" {
  default = "t2.micro"
}
```


main.tf
```
resource "aws_instance" "webserver" {
  ami = var.ami
  instance_type = var.instance_type
}
```



#### Resource attributes - Interpolation sequence - having a block depending on other block resource


```
resource "local_file" "pet" {
  filename = var.filename
  content = "My favorite pet is ${random_pet.my-pet.id}"
}

resource "random_pet" "my-pet" {
  prefix = var.prefix
  separator = var.separator
  length = var.length
}
```

Example:

```
resource "time_static" "time_update" {
}

resource "local_file" "time" {
    filename = "/root/time.txt"
    content = "Time stamp of this file is ${time_static.time_update.id}"
}
```

```
❯ cat /root/time.txt 
Time stamp of this file is 2024-03-09T16:24:31Z
```

#### Explicitly dependency 

```
resource "local_file" "whale" {
  filename = "/root/whale"
  content = "whale"
  depends_on = [
    local_file.krill
  ]
}

resource "local_file" "krill" {
  filename = "/root/krill"
  content = "krill"
}
```




#### Terraform show

```
❯ terraform show
# local_file.time:
resource "local_file" "time" {
    content              = "Time stamp of this file is 2024-03-09T16:24:31Z"
    content_base64sha256 = "VwdFKZLAVneRDfsGC3HdQwHSeh/DFYA1eszgvmUDgpw="
    content_base64sha512 = "+k2oL0ulqv4FFsHaKEc2GJEQ7XlEohlrwt8KkZ0Zl9IXksbyOLqHl8exXooao7+uLyelw7bmky1MDQ79+dolLA=="
    content_md5          = "27d0318efb0d86b11b34b5bd72f53b9e"
    content_sha1         = "c5e019435bbd74ce01fab15723d99bad5e8bff49"
    content_sha256       = "5707452992c05677910dfb060b71dd4301d27a1fc31580357acce0be6503829c"
    content_sha512       = "fa4da82f4ba5aafe0516c1da284736189110ed7944a2196bc2df0a919d1997d21792c6f238ba8797c7b15e8a1aa3bfae2f27a5c3b6e6932d4c0d0efdf9da252c"
    directory_permission = "0777"
    file_permission      = "0777"
    filename             = "/root/time.txt"
    id                   = "c5e019435bbd74ce01fab15723d99bad5e8bff49"
}

# time_static.time_update:
resource "time_static" "time_update" {
    day     = 9
    hour    = 16
    id      = "2024-03-09T16:24:31Z"
    minute  = 24
    month   = 3
    rfc3339 = "2024-03-09T16:24:31Z"
    second  = 31
    unix    = 1710001471
    year    = 2024
}
```


- Lets see another example using the provider "tls_private_key" 


```
resource "tls_private_key" "pvtkey" {
  algorithm = "RSA"
  rsa_bits = 4096
}
```


- The tls_private_key generates a secure private key and encodes it as PEM and it lives only on terraform state, we can see it with terraform show command:


```
❯ terraform show
# tls_private_key.pvtkey:
resource "tls_private_key" "pvtkey" {
    algorithm                     = "RSA"
    ecdsa_curve                   = "P224"
    id                            = "78503bcbf6a55bb3162fdfa63f0c97bb901d8d1c"
    private_key_openssh           = (sensitive value)
    private_key_pem               = (sensitive value)
    private_key_pem_pkcs8         = (sensitive value)
    public_key_fingerprint_md5    = "9e:4a:94:ec:d3:21:86:e1:78:45:f3:97:b2:e8:df:2e"
    public_key_fingerprint_sha256 = "SHA256:jUl5LeusFdgANJLY+qyGIZ737E8pCyS+W5TLdDT9gws"
    public_key_openssh            = <<-EOT
        ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCiCZwx0lqa77HkRLCSUouiCvLesLuWdQV+DrwhYZ0PrqvDfiyzzgVlWfHGyMpYiGoQPNLE++CqNbo2bWlPlyGTl7DTrwHFNroL1e+4bHg+IThxhU1rkC5gev7RK6zRbhYCWuehdpE97+eNyi1grBr5RQMEmGcTgfERGiNSp5or8UTlifMtLpqf4o7ZrjP5oXMvBaOSe8C6XJcKDaasQNl5zXo5XByUmB0spATEYE/BHBEyNjuL7mEVCiSPLsvO1zL4QAHJMxI8660aeDEQMQeA5H05DItEpD3x0l760zCZ+CgLQosH0HS3B6A7mifnRV7Po2CyR91R6kYu5Wo6wLLQP/x+5wgm9l9v9wP/l5iyfTyWXayvxlnbz/1h3CJqke/ZMjgfAkOrU0gPVzSoc2/KleCPGC5FV0EynPdtEJloe4zD8CXs7y3xPz/feiP8jCa98HoMgLY5Z8xk5EPqQc/qx1htPGili153exMF3ljDPFAyJvI0rbd3KkO1YGavQrhOZ33vpm3ml312n4xbUbJOeUDnZW5JnNcUrophVPagvEarLZCk1i2+rD3aeLFnIec4w5yS1At5xz7xTAIWLSaKkf3ClHBykAUdYdJAfmOEQZVJbHyZ+GbuTOgR6+HtymMIq+JKPD+C3lOspSTSd1+nYCFMmcTSp1qg1vQAgKZ3UQ==
    EOT
    public_key_pem                = <<-EOT
        -----BEGIN PUBLIC KEY-----
        MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAogmcMdJamu+x5ESwklKL
        ogry3rC7lnUFfg68IWGdD66rw34ss84FZVnxxsjKWIhqEDzSxPvgqjW6Nm1pT5ch
        k5ew068BxTa6C9XvuGx4PiE4cYVNa5AuYHr+0Sus0W4WAlrnoXaRPe/njcotYKwa
        +UUDBJhnE4HxERojUqeaK/FE5YnzLS6an+KO2a4z+aFzLwWjknvAulyXCg2mrEDZ
        ec16OVwclJgdLKQExGBPwRwRMjY7i+5hFQokjy7Lztcy+EAByTMSPOutGngxEDEH
        gOR9OQyLRKQ98dJe+tMwmfgoC0KLB9B0twegO5on50Vez6NgskfdUepGLuVqOsCy
        0D/8fucIJvZfb/cD/5eYsn08ll2sr8ZZ28/9YdwiapHv2TI4HwJDq1NID1c0qHNv
        ypXgjxguRVdBMpz3bRCZaHuMw/Al7O8t8T8/33oj/IwmvfB6DIC2OWfMZORD6kHP
        6sdYbTxopYted3sTBd5YwzxQMibyNK23dypDtWBmr0K4Tmd976Zt5pd9dp+MW1Gy
        TnlA52VuSZzXFK6KYVT2oLxGqy2QpNYtvqw92nixZyHnOMOcktQLecc+8UwCFi0m
        ipH9wpRwcpAFHWHSQH5jhEGVSWx8mfhm7kzoEevh7cpjCKviSjw/gt5TrKUk0ndf
        p2AhTJnE0qdaoNb0AICmd1ECAwEAAQ==
        -----END PUBLIC KEY-----
    EOT
    rsa_bits                      = 4096
}
```


- lets now create a file with the our private key using the local_file provider:

```
resource "tls_private_key" "pvtkey" {
  algorithm = "RSA"
  rsa_bits = 4096
}

resource "local_file" "key_details" {
  filename = "/root/key.txt"
  content = tls_private_key.pvtkey.private_key_pem
}
```

- Lets see now the content of our file:

```
❯ cat /root/key.txt 
-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
```


#### Terraform output



```
resource "local_file" "pet" {
  filename = var.filename
  content = "My favorite pet is ${random_pet.my-pet.id}"
}

resource "random_pet" "my-pet" {
  prefix = var.prefix
  separator = var.separator
  length = var.length
}

output pet-name {
  value = random_pet.my-pet.id
  description = "Record value of id during random_pet resource"
}
```

- During our terraform apply our output will show the new variable pet-name and the value 
- We can also use terraform output

```
$ terraform output
pet-name = Mrs.gibbon

OR

$ terraform output pet-name
Mrs.gibbon
```

- We can use output variables when we want show variables to the screen or use in other scripts and Ansible


### Terraform commands


```
$ terraform init
$ terraform plan
$ terraform apply
$ terraform validate # to validate the .tf file
$ terraform fmt # it formate the code for visibility like indentation 
$ terraform show # show all resources created by terraform and its properties
$ terraform show -json # show all resources in JSON format
$ terraform providers # show all providers set up 
$ terraform providers mirror /root/terraform/new_local_file # copy provider plugin to a new location 
$ terraform output # show all TF variables 
$ terraform refresh # update TF.state if any manual update on the infrastructure side
$ terraform graph # generates a graph file of TF infra
$ terraform graph | dot -Tsvg > graph.svg (need to install graphviz package)
```

### Mutable and Immutable Infrastructure 

- Mutable is what you change
- Immutable is what you don't change
- When you change a TF script to change a file_permission from 0777 to 0700 terraform first delete the resource and then it recreates with the correct permission
- Mutable example is when you install a nginx 1.16 on a server and then updates it to nginx 1.17 and then nginx 1.18. This is called Mutable.
- Immutable is when provision a new VSI instead of updating your old one. Once you provision a new one the old one is deleted this is reached using variable create_before_destroy.
- The default TF behavior is to delete the resource and then create it again with the new properties. Lets have a look at the lifecycle statement and variable create_before_destroy.


```
resource "local_file" "pet" {
  filename = "/root/pets.txt"
  content = "We love pets!"
  file_permission = "0700"

  lifecycle {
    create_before_destroy = true
  }
}
```

- With this statement TF will create a new file and then delete the old one with previously properties
- There will be situations we don't want to destroy the old resource at all. For this we can use the property prevent_destroy

```
resource "local_file" "pet" {
  filename = "/root/pets.txt"
  content = "We love pets!"
  file_permission = "0700"

  lifecycle {
    prevent_destroy = true
  }
}
```


- We can also ignore changes that are made outside of terraform. Usually the TF will try to change back to the state set into the TF scripts. For example if your TF has a tag name=serverA and you manually changed manually to name=serverB when you run TF script it will move back to name=serverA accordingly to what is set into the TF script. When we use ignore_changes to the tag property, the TF will not move back to serverA it will keep what you changed manually and it will ignore the change you made manually. You can use `ignore_changes = all` also

```
resource "local_file" "pet" {
  filename = "/root/pets.txt"
  content = "We love pets!"
  file_permission = "0700"

  lifecycle {
    ignore_changes = [
      tags,ami
    ]
  }
}
```


- Lets see another example using lifecycle create_before_destroy


```
resource "local_file" "file" {
    filename = var.filename
    file_permission =  var.permission
    content = random_string.string.id
    
}

resource "random_string" "string" {
    length = var.length
    keepers = {
        length = var.length
    }
    lifecycle {
        create_before_destroy = true
    }      
}
```


### Data sources 


- We can still read a manual created file with TF script. Lets consider you created manually a file in /root/dog.txt wih content "Dogs are awesome!", lets see how TF can read this file and still use it as reference to any other object 


```
$ cat /root/dog.txt
Dogs are awesome!
```


```
resource "local_file" "pet" {
  filename = "/root/pets.txt"
  content = data.local_file.dog.content
}

data "local_file" "dog" {
  filename = "/root/dog.txt"
}
```

- For more examples look for data sources TF documentation 

- Lets see another example using data source and reading a file from OS:

```
output "os-version" {
  value = data.local_file.os.content
}
data "local_file" "os" {
  filename = "/etc/os-release"
}
```

- Another examples:

```
data "aws_s3_bucket" "selected" {
  bucket = "bucket.test.com"
}
```

```
data "aws_ebs_volume" "gp2_volume" {
  most_recent = true

  filter {
    name   = "volume-type"
    values = ["gp2"]
  }
}
```

## Count

- We can use the variable count to create the same resource many times. 
- Because we can not create 3 files with the same name terraform will try to create 3 files and replace the other one.
- To workaround we can create a variable filename with a list of 03 filenames
  

```
resource "local_file" "pet {
  filename = var.filename

  count = 3
}
```

```
variable "filename" {
  default = [
    "/root/pets.txt",
    "/root/dogs.txt",
    "/root/cats.txt"
  ]
}
```

- If we have many filenames and we don't know how many, we can use a internal function length to count how many item there is in that list

```
resource "local_file" "pet {
  filename = var.filename

  count = length(var.filename)
}
```

- We can also have other different functions 
- TF consider this count function as a list and a list has order: item0, item1 and item2
- If we delete the first item called item0, TF will destroy item0 and recreate as dog, will destroy and recreate as cats and will destroy item3
  
  - Lets see one more nice example:

```
resource "local_sensitive_file" "name" {
    filename = "/root/user-data"
    content = "password: S3cr3tP@ssw0rd"

}
```

variable.tf
```
variable "users" {
    type = list(string)
    default = [ "/root/user10", "/root/user11", "/root/user12", "/root/user10"]
}
variable "content" {
    default = "password: S3cr3tP@ssw0rd"
  
}
```


## For_each

- As we know the count function is consider as a list, and list are indexed and can not be deleted and when we do all items from the list is destroyed and recreated.
- To workaround on this issue we can use other function called for_each
- For_each argument works only as a map or a set, not a list.

```
resource "local_file" "pet" {
  filename = each.value 
  for_each = var.filename
}

variable "filename" {
  type=set(string)
  default = [
    "/root/pets.txt",
    "/root/dogs.txt",
    "/root/cats.txt"
  ]
}
```

- Another way of workaround on this issue is to use function toset, and in this case we can use a list of filename

```
resource "local_file" "pet" {
  filename = each.value 
  for_each = toset(var.filename)
}
```

```
variable "filename" {
  type=list(string)
  default = [
    "/root/pets.txt",
    "/root/dogs.txt",
    "/root/cats.txt"
  ]
}
```

- In this example the output if we run terraform output, TF will show the output as a map and not as list, so map has no index and will bypass the list issue when we delete a item in the list.

- Lets see another example:

```
resource "local_sensitive_file" "name" {
    filename = each.value
    content = var.content
    for_each = toset(var.users)

}
```

variables.tf
```
variable "users" {
    type = list(string)
    default = [ "/root/user10", "/root/user11", "/root/user12", "/root/user10"]
}
variable "content" {
    default = "password: S3cr3tP@ssw0rd"
  
}
```


### Terraform Version

- Usually TF downloads the latest version of each provider.
- Lets say you want to change the version of a provider local. Go to Terraform Registry https://registry.terraform.io/providers and search for local. Ie. https://registry.terraform.io/providers/hashicorp/local/2.3.0 change the version on the top header and then click in "User Provider" you will see a code like this to add to your TF scripts 

```
terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
      version = "2.3.0"
    }
  }
}
```


