# Python

## Python version

We can have python version 2.7 and python version 3 in the same node. Exmample:

```
thor@host01 ~$ python --version
Python 2.7.5
```

```
thor@host01 ~$ python3 --version
Python 3.6.8
```


## Installing python 3.6

```
$ sudo yum install python36
```


## Python example code

```
thor@host01 ~$ cat main.py 
import sys

def print_message():
   if sys.version_info[0] < 3:
     print("Hello old World!")
   else:
     print("Hello new World!")

if __name__ == '__main__':
    print_message()
```


### Using python2 and python3 to run a python app

```
thor@host01 ~$ python2 main.py 
Hello old World!

thor@host01 ~$ python3 main.py 
Hello new World!

```


## What is the python version used by pip

```
thor@host01 ~$ pip -V
pip 21.3.1 from /usr/lib/python3.6/site-packages/pip (python 3.6)
```


### Install a flask app with pip

```
thor@host01 ~$ sudo pip install flask
Collecting flask
  Downloading Flask-2.0.3-py3-none-any.whl (95 kB)
     |████████████████████████████████| 95 kB 1.5 MB/s             
Collecting itsdangerous>=2.0
  Downloading itsdangerous-2.0.1-py3-none-any.whl (18 kB)
Collecting Jinja2>=3.0
  Downloading Jinja2-3.0.3-py3-none-any.whl (133 kB)
     |████████████████████████████████| 133 kB 30.3 MB/s            
Collecting click>=7.1.2
  Downloading click-8.0.4-py3-none-any.whl (97 kB)
     |████████████████████████████████| 97 kB 11.5 MB/s            
Collecting Werkzeug>=2.0
  Downloading Werkzeug-2.0.3-py3-none-any.whl (289 kB)
     |████████████████████████████████| 289 kB 3.8 MB/s            
Collecting importlib-metadata
  Downloading importlib_metadata-4.8.3-py3-none-any.whl (17 kB)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.0.1-cp36-cp36m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (30 kB)
Collecting dataclasses
  Downloading dataclasses-0.8-py3-none-any.whl (19 kB)
Collecting zipp>=0.5
  Downloading zipp-3.6.0-py3-none-any.whl (5.3 kB)
Collecting typing-extensions>=3.6.4
  Downloading typing_extensions-4.1.1-py3-none-any.whl (26 kB)
Installing collected packages: zipp, typing-extensions, MarkupSafe, importlib-metadata, dataclasses, Werkzeug, Jinja2, itsdangerous, click, flask
Successfully installed Jinja2-3.0.3 MarkupSafe-2.0.1 Werkzeug-2.0.3 click-8.0.4 dataclasses-0.8 flask-2.0.3 importlib-metadata-4.8.3 itsdangerous-2.0.1 typing-extensions-4.1.1 zipp-3.6.0
WARNING: Target directory /usr/lib/python3.6/site-packages/__pycache__ already exists. Specify --upgrade to force replacement.
WARNING: Target directory /usr/lib/python3.6/site-packages/bin already exists. Specify --upgrade to force replacement.
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
```


### Checking if a package is installed



```
thor@host01 ~$ pip show Jinja2
Name: Jinja2
Version: 3.0.3
Summary: A very fast and expressive template engine.
Home-page: https://palletsprojects.com/p/jinja/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD-3-Clause
Location: /home/thor/.local/lib/python3.6/site-packages
Requires: MarkupSafe
Required-by: Flask
```

We can check several packages also

```
thor@host01 ~$ pip show  Jinja2 Werkzeug markupsafe
Name: Jinja2
Version: 3.0.3
Summary: A very fast and expressive template engine.
Home-page: https://palletsprojects.com/p/jinja/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD-3-Clause
Location: /home/thor/.local/lib/python3.6/site-packages
Requires: MarkupSafe
Required-by: Flask
---
Name: Werkzeug
Version: 2.0.3
Summary: The comprehensive WSGI web application library.
Home-page: https://palletsprojects.com/p/werkzeug/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD-3-Clause
Location: /home/thor/.local/lib/python3.6/site-packages
Requires: dataclasses
Required-by: Flask
---
Name: MarkupSafe
Version: 2.0.1
Summary: Safely add untrusted strings to HTML/XML markup.
Home-page: https://palletsprojects.com/p/markupsafe/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD-3-Clause
Location: /home/thor/.local/lib/python3.6/site-packages
Requires: 
Required-by: Jinja2
```


### python requirements packages files

```
thor@host01 ~$ cat requirements.txt 
Flask==0.10.1
Jinja2==2.7.3
MarkupSafe==0.23
Werkzeug==0.9.6
requests==2.3.0
gunicorn==18.0
```

#### Installing requirements packages with requirements file

```
thor@host01 ~$ sudo pip install -r requirements.txt 
Collecting Flask==0.10.1
  Downloading Flask-0.10.1.tar.gz (544 kB)
     |████████████████████████████████| 544 kB 4.8 MB/s            
  Preparing metadata (setup.py) ... done
Collecting Jinja2==2.7.3
  Downloading Jinja2-2.7.3.tar.gz (378 kB)
     |████████████████████████████████| 378 kB 75.7 MB/s            
  Preparing metadata (setup.py) ... done
Collecting MarkupSafe==0.23
  Downloading MarkupSafe-0.23.tar.gz (13 kB)
  Preparing metadata (setup.py) ... done
Collecting Werkzeug==0.9.6
  Downloading Werkzeug-0.9.6.tar.gz (1.1 MB)
     |████████████████████████████████| 1.1 MB 30.8 MB/s            
  Preparing metadata (setup.py) ... done
Collecting requests==2.3.0
  Downloading requests-2.3.0-py2.py3-none-any.whl (452 kB)
     |████████████████████████████████| 452 kB 53.9 MB/s            
Collecting gunicorn==18.0
  Downloading gunicorn-18.0-py33-none-any.whl (93 kB)
     |████████████████████████████████| 93 kB 3.4 MB/s             
Collecting itsdangerous>=0.21
  Using cached itsdangerous-2.0.1-py3-none-any.whl (18 kB)
Using legacy 'setup.py install' for Flask, since package 'wheel' is not installed.
Using legacy 'setup.py install' for Jinja2, since package 'wheel' is not installed.
Using legacy 'setup.py install' for MarkupSafe, since package 'wheel' is not installed.
Using legacy 'setup.py install' for Werkzeug, since package 'wheel' is not installed.
Installing collected packages: MarkupSafe, Werkzeug, Jinja2, itsdangerous, requests, gunicorn, Flask
    Running setup.py install for MarkupSafe ... done
    Running setup.py install for Werkzeug ... done
    Running setup.py install for Jinja2 ... done
    Running setup.py install for Flask ... done
Successfully installed Flask-0.10.1 Jinja2-2.7.3 MarkupSafe-0.23 Werkzeug-0.9.6 gunicorn-18.0 itsdangerous-2.0.1 requests-2.3.0
WARNING: Target directory /usr/lib/python3.6/site-packages/werkzeug already exists. Specify --upgrade to force replacement.
WARNING: Target directory /usr/lib/python3.6/site-packages/flask already exists. Specify --upgrade to force replacement.
WARNING: Target directory /usr/lib/python3.6/site-packages/markupsafe already exists. Specify --upgrade to force replacement.
WARNING: Target directory /usr/lib/python3.6/site-packages/itsdangerous-2.0.1.dist-info already exists. Specify --upgrade to force replacement.
WARNING: Target directory /usr/lib/python3.6/site-packages/itsdangerous already exists. Specify --upgrade to force replacement.
WARNING: Target directory /usr/lib/python3.6/site-packages/jinja2 already exists. Specify --upgrade to force replacement.
WARNING: Target directory /usr/lib/python3.6/site-packages/bin already exists. Specify --upgrade to force replacement.
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

```


### Upgrade gunicorn version


#### Checking current version 

```
thor@host01 ~$ pip show gunicorn
Name: gunicorn
Version: 18.0
Summary: WSGI HTTP Server for UNIX
Home-page: http://gunicorn.org
Author: Benoit Chesneau
Author-email: benoitc@e-engura.com
License: MIT
Location: /home/thor/.local/lib/python3.6/site-packages
Requires: 
Required-by: 
```

#### Upgrading gunicorn version 

```
thor@host01 ~$ pip install gunicorn --upgrade
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: gunicorn in ./.local/lib/python3.6/site-packages (18.0)
Collecting gunicorn
  Downloading gunicorn-21.2.0-py3-none-any.whl (80 kB)
     |████████████████████████████████| 80 kB 4.2 MB/s             
Requirement already satisfied: packaging in /usr/lib/python3.6/site-packages (from gunicorn) (21.3)
Requirement already satisfied: importlib-metadata in ./.local/lib/python3.6/site-packages (from gunicorn) (4.8.3)
Requirement already satisfied: typing-extensions>=3.6.4 in ./.local/lib/python3.6/site-packages (from importlib-metadata->gunicorn) (4.1.1)
Requirement already satisfied: zipp>=0.5 in ./.local/lib/python3.6/site-packages (from importlib-metadata->gunicorn) (3.6.0)
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/lib/python3.6/site-packages (from packaging->gunicorn) (3.1.1)
Installing collected packages: gunicorn
  Attempting uninstall: gunicorn
    Found existing installation: gunicorn 18.0
    Uninstalling gunicorn-18.0:
      Successfully uninstalled gunicorn-18.0
Successfully installed gunicorn-21.2.0
```


#### Checking gunicorn version after upgrade

```
thor@host01 ~$ pip show gunicorn
Name: gunicorn
Version: 21.2.0
Summary: WSGI HTTP Server for UNIX
Home-page: https://gunicorn.org
Author: Benoit Chesneau
Author-email: benoitc@gunicorn.org
License: MIT
Location: /home/thor/.local/lib/python3.6/site-packages
Requires: importlib-metadata, packaging
Required-by: 
```


### Uninstalling gunicorn 

```
thor@host01 ~$ sudo pip uninstall gunicorn
Found existing installation: gunicorn 21.2.0
Uninstalling gunicorn-21.2.0:
  Would remove:
    /usr/lib/python3.6/site-packages/gunicorn-21.2.0.dist-info/*
    /usr/lib/python3.6/site-packages/gunicorn/*
Proceed (Y/n)? Y
  Successfully uninstalled gunicorn-21.2.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
```


```
thor@host01 ~$ sudo pip uninstall gunicorn
Found existing installation: gunicorn 18.0
Uninstalling gunicorn-18.0:
  Would remove:
    /usr/lib/python3.6/site-packages/gunicorn-18.0.dist-info/*
Proceed (Y/n)? Y
  Successfully uninstalled gunicorn-18.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv


thor@host01 ~$ pip show gunicorn
WARNING: Package(s) not found: gunicorn
```
