from django.urls import path
from . import views


app_name = 'contact'

urlpatterns = [
    path('', views.view_contacts, name='contact'),
    
]