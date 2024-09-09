from django.shortcuts import render
from .models import WorkExperience, Education
# Create your views here.

def resume_view(request):
    experiences = WorkExperience.objects.all()
    educations = Education.objects.all()
    
    '''
    context= {
        "variable name in template": "variable name in view"
    }
    '''
    return render(request,'resume/resume.html',context={'experiences':experiences, 'educations':educations})
    