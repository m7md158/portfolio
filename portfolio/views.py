from django.shortcuts import render
from .models import Job, Category
# Create your views here.
def job_list(request):
    
    jobs = Job.objects.all()
    
    return render(request, 'portfolio/job_list.html',context={'jobs':jobs})

def job_detail(request,id):
    
    job_detail = Job.objects.get(id=id)
    
    return render(request, 'portfolio/job_detail.html',context={'job_detail' : job_detail})