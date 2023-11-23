from django.db import models
from countryapp.models import Country
# Create your models here.
class State(models.Model):
    id = models.BigAutoField(primary_key=True,db_column='id')
    state_name = models.CharField(max_length=120,db_column='state_name',null=True,unique=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,db_column='country_id',null=True)
    
    class Meta:
        db_table = 'states'