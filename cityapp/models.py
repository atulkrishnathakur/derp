from django.db import models
from stateapp.models import State
from countryapp.models import Country
# Create your models here.
class City(models.Model):
    id = models.BigAutoField(primary_key=True,db_column='id')
    city_name = models.CharField(max_length=120,db_column='city_name',null=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,db_column='country_id',null=True)
    state = models.ForeignKey(State,on_delete=models.CASCADE,db_column='state_id',null=True)

    class Meta:
        db_table = 'cities'