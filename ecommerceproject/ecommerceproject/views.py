from django.shortcuts import redirect
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
	return redirect('/home/')

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
   
# info@abriendomen return redirect('/home')
