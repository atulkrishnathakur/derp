from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from countryapp.models import Country
from stateapp.models import State
from cityapp.models import City
from django.template import loader
from django.shortcuts import redirect
from django.urls import reverse
from . import apps

app_name = apps.CityappConfig.name

def list(request):
    try:
        cities = City.objects.select_related('state').all()

        #print(cities.query) # use to print query
        context = {
            'appname':app_name,
            'cities':cities
        }
        return render(request,'cityapp/list.html',context)
    except Exception as e:
        print(e)
def create(request):
    try:
        if request.method == 'GET':
            countries = Country.objects.all()
            context = {
                'countries':countries
            }
            return render(request,'cityapp/create.html',context)
        if request.method == 'POST':
            countries = Country.objects.all()
            errorlist = {}
            countryid = request.POST['countryid']
            state_name = request.POST['statename']
            if countryid == "":
                errorlist['country_name_err'] = 'Country name is required' 
            if state_name == "":
                errorlist['state_name_err'] = 'State name is required'
            elif state_name.isnumeric():
                errorlist['state_name_err'] = 'Enter correct state name'     
            if(len(errorlist) != 0):
                context = {
                    'countries':countries,
                    'errorlist':errorlist
                }
                return render(request,'stateapp/create.html',context)
            else:
                stateobj = State(country_id=countryid,state_name=state_name)
                stateobj.save()
                return HttpResponseRedirect(reverse("stateapp:list"))
    except Exception as e:
        print(e)
        context = {}
        return render(request,'stateapp/create.html',context)

def getStateByAjax(request):
    try:
        if request.method == 'POST':
            country_id  = request.POST.get('country_id')
            states = State.objects.get(country_id=country_id)
            context = {
                "states":states
            }
            return JsonResponse(context)
        else:
            
    except Exception as e:
        print(e)

def deleterecored(request, id):
    try:
        if request.method == "GET":
            state = State.objects.get(id = id)
            state.delete()
            return redirect('stateapp:list')
        else:
            return redirect('stateapp:list')
    except Exception as e:
        print(e)

def edit(request, id):
    try:
        if request.method == 'GET':
            state = State.objects.get(id = id)
            countries = Country.objects.all().values()
            context = {
                'state':state,
                'countries':countries
            }
            return render(request,'stateapp/edit.html',context)
        if request.method == 'POST':
            state = State.objects.get(id = id)
            countries = Country.objects.all().values()
            errorlist = {}
            stateobj = State.objects.get(id = id)
            state_name = request.POST['statename']
            country_id = request.POST['countryid']
            if country_id == "":
                errorlist['country_name_err'] = "Country is required"
            if state_name == "":
                errorlist['state_name_err'] = 'State name is required'
            elif state_name.isnumeric():
                errorlist['state_name_err'] = 'Enter correct state name'    
            if(len(errorlist) != 0):
                context = {
                    'errorlist':errorlist,
                    'state':state,
                    'countries':countries
                }
                return render(request,'stateapp/edit.html',context)
            else:
                stateobj.country_id = country_id
                stateobj.state_name = state_name
                stateobj.save()
                return HttpResponseRedirect(reverse("stateapp:list"))
    except Exception as e:
        print(e)
        state = State.objects.get(id = id) 
        countries = Country.objects.all().values()
        context = {
            'state':state,
            'countries':countries
        }
        return render(request,'stateapp/edit.html',context)