# install mysqlclient
```
ATUL@DESKTOP-21EPCLH MINGW64 /i/mydjangofirst/derp (main)
$ pip install mysqlclient
Requirement already satisfied: mysqlclient in i:\mydjangofirst\venv\lib\site-packages (2.1.1)
```

# Requirements txt
```
ATUL@DESKTOP-21EPCLH MINGW64 /i/mydjangofirst/derp (main)
$ python -m pip freeze > requirements.txt
(venv) 
```

# django-extensions
1. https://django-extensions.readthedocs.io/en/latest/installation_instructions.html 
2. install 
```
$ pip install django-extensions
```

2. Check installation
```
ATUL@DESKTOP-21EPCLH MINGW64 /i/mydjangofirst/derp (v1-user-management-app)
$ python manage.py shell
Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> import django_extensions
>>> django_extensions.VERSION
(3, 2, 3)
>>>
```
3. configuration
```
INSTALLED_APPS = [
   ........,
    'django_extensions',
    ..........
]
```

# create superuser
```
ATUL@DESKTOP-21EPCLH MINGW64 /i/mydjangofirst/derp (v1-user-management-app)
$ python manage.py createsuperuser
Username: abc     
Email address: abc@yopmail.com
Password: 
Password (again):
←[31;1mThis password is too common.
This password is entirely numeric.
←[0mBypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(venv) 
```

1. type in URL http://localhost:8000/admin

# Register model to show in administration for super user 
```
from django.contrib import admin

# Register your models here.
from .models import CustomUser

admin.site.register(CustomUser)
```
