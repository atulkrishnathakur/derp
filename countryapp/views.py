from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from countryapp.models import Country
from django.template import loader
from django.shortcuts import redirect
from django.urls import reverse
from . import apps

app_name = apps.CountryappConfig.name

def list(request):
    try:
        countries = Country.objects.all()
        context = {
            'appname':app_name,
            'countries':countries
        }
        return render(request,'countryapp/list.html',context)
    except Exception as e:
        print(e)
def create(request):
    try:
        if request.method == 'GET':
            context = {}
            return render(request,'countryapp/create.html',context)
        if request.method == 'POST':
            errorlist = {}
            country_name = request.POST['countryname']
            if country_name == "":
                errorlist['country_name_err'] = 'Country name is required'
            elif country_name.isnumeric():
                errorlist['country_name_err'] = 'Enter correct country name'    
            if(len(errorlist) != 0):
                context = {
                    'errorlist':errorlist
                }
                return render(request,'countryapp/create.html',context)
            else:
                countryobj = Country(country_name=country_name)
                countryobj.save()
                return HttpResponseRedirect(reverse("countrylist"))
    except Exception as e:
        print(e)
        context = {}
        return render(request,'countryapp/create.html',context)