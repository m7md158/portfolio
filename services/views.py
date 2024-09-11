from django.shortcuts import render
from .models import Service
# Create your views here.
def services_view(request):
    services = Service.objects.all()
    
    
    return render(request, 'services/services.html', context={'services':services})