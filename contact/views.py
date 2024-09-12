from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        from_email = request.POST.get('from_email')
        message = request.POST.get('message')
    
        # send email
        if from_email and message and name:
            try:
                email = EmailMessage(
                    subject= name, # subject
                    body=message, # message
                    from_email=from_email, # from email 
                    to =['mohammed.qabil15@gmail.com'], # to email
                    headers={'Reply-To': from_email}
                    )
                email.send(fail_silently=False)
                return HttpResponse("Email sent successfully!")
            except Exception as e:
                return HttpResponse(f"Failed to send email: {str(e)}")
            
            else:
                return HttpResponse("Invalid form submission.")
                 
                
    return render(request, 'contact/contact.html')

