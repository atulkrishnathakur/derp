from django.db import models

# Create your models here.
class Country(models.Model):
    id = models.BigAutoField(primary_key=True,db_column='id')
    country_name = models.CharField(max_length=120,db_column='country_name',null=True,unique=True)
    
    class Meta:
        db_table = 'countries'