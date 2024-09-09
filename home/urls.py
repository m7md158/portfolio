from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    # Add your other URL patterns here
]