from django.shortcuts import render
from .models import Contact, Contact

from django.contrib import messages
from django.core.mail import send_mail

from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def experience(request):
    return render(request, 'experince.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        message=request.POST['message']
        send_mail(
            '@SPSK',
            'thank you for contacting us.. wee will respond soon...',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        if len(name) < 2 or len(email) < 10 or len(number) < 10 or len(message) < 5:
            messages.error(request, 'PLEASE FIIL ALL REQUIRED FILED IN CORRECT WAY....')
        else:
            contact=Contact(name=name, email=email, number=number, message=message)
            contact.save()
            messages.success(request, 'FORM SUBMITED SUCCESSFULLY...')
    return render(request, 'contact.html')

def calculator(request):
    return render(request, 'calculator.html')


def validation(request):
    return render(request, 'validation.html')