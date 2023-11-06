from django.shortcuts import render
from django.http import HttpResponse
from countryapp.models import Country 

def list(request):
    return render(request,'countryapp/list.html')
def create(request):
    return render(request,'countryapp/create.html')
def savecountry(request):
    try:
        if request.method == 'POST':
            country_name = request.POST['countryname']
            countryobj = Country(country_name=country_name)
            countryobj.save()
            return redirect('countrylist')
    except Exception as e:
        print(e)    

