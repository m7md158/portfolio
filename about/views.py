from django.shortcuts import render
from .models import User, Profile, Skills
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
# Create your views here.

def about_view(request):
    skills  = Skills.objects.all()
    profiles = Profile.objects.all()
    
    
    
    '''
    context= {
        "variable name in template": "variable name in view"
    }
    '''
    
    return render(request,"about/about.html",context={ 'skills' : skills , 'profiles' : profiles})

