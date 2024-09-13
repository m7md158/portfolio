from django.urls import path
from . import views
from . import api

app_name = 'services'

urlpatterns = [
    path('', views.services_view, name='services'),
    ## CBV
    path('api', api.ServiceList.as_view(), name='services_list'),
    path('api/<int:id>', api.ServiceDetail.as_view(), name='services_detail'),
   
]