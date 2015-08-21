from django.shortcuts import redirect
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
	return redirect('/home/')
   
# info@abriendomen return redirect('/home')
