from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20,null=True,db_column='phone')
    
    class Meta:
        db_table = 'auth_user'