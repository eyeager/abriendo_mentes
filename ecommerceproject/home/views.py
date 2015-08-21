from django.shortcuts import render

from django.shortcuts import redirect
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'home/index.html', {})

def contact(request):
	return render(request, 'home/contact.html', {})

def sent(request):
	print 'sent'
	name = request.POST['InputName']
	email = request.POST['InputEmail']
	message = request.POST['InputMessage']
	subject = request.POST['InputSubject']
	send_mail('Subject here', message, email,
	['gmdavis1@gmail.com'], fail_silently=False)
	return redirect('/contact')

def whoweare(request):
	return render(request, 'home/who_we_are.html', {})