from django.urls import path
from . import views

app_name = 'certification'


urlpatterns = [
    path('', views.certificates, name='certification'),
    
    # CBV
]