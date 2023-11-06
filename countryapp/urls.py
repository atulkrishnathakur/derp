from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='countries'),
    path('list', views.list, name='countrylist'),
    path('create', views.create, name='countrycreate'),
    path('savecountry', views.savecountry, name='savecountry'),
]