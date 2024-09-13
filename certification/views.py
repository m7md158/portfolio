from django.shortcuts import render
from .models import Certificate
# Create your views here.

def certificates(request):
    certificates = Certificate.objects.all() 
    
    return render(request, 'certification/certification.html',{'certificates':certificates})
