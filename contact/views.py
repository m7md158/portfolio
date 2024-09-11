from django.shortcuts import render


# Create your views here.
def view_contacts(request):

    
    return render(request,'contact/contact.html')