from django.urls import path
from . import views


app_name = 'contact'

urlpatterns = [
    path('', views.view_contacts, name='contact'),
    # Add your other URL patterns here
]