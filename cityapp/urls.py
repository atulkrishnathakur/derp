from django.urls import path
from . import views
from . import apps

app_name = apps.CityappConfig.name

urlpatterns = [
    path('', views.list, name='cities'),
    path('list', views.list, name='list'),
    path('create', views.create, name='create'),
    path('delete/<int:id>', views.deleterecored, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('get-state-ajax', views.getStateByAjax, name='get_state_ajax'),
]