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

# Create URLs
1. create an urls.py file in app directory
2. add urls in this file

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='countries'),
    path('list', views.list, name='countrylist'),
]
```
3. open the derp/derp/urls.py file and add the below code

```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('country/',include('countryapp.urls'))
]
```

# How to create template
1. create a base template directory in porject directory like derp/templates/. This is the sibling of manage.py file.
2. Now configrue the base templates directory
3. open the setting.py file and write bellow code

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

4. create the templates directory in app directory like countryapp/templates/
5. create the countryapp directory inside templates directory like countryapp/templates/countryapp/
6. create the list.html file like countryapp/templates/countryapp/list.html

# Render a template file

```
from django.shortcuts import render
from django.http import HttpResponse

def list(request):
    return render(request,'countryapp/list.html')

```

# Extends the base html file
1. creata a base.html file in project template directory like *derp/templates/base.html

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Title</title>
    </head>
    <body>
        {% block content %}
        {% endblock %}
    </body>
</html>

```
2. extends base.html into derp/templates/countryapp/list.html. Here "content" is the name of block

```
{% extends 'base.html' %}
{% block content %}
<h1>Home Page</h1>
{% endblock content %}

```
# static for css,image and javaScript

1. write the code in setting.py file

```
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```
2. create the static directory in app directory like countryapp/static/
3. create the countryapp directory inside static directory like countryapp/static/countryapp/
4. create the css directory inside countryapp directory like countryapp/static/countryapp/css/
5. create the style.css directory inside css directory like countryapp/static/countryapp/css/style.css
