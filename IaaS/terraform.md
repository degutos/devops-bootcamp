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




### Variables to create an AWS resource

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



