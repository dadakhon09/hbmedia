from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

def index(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def contact(request):
	return render(request, 'contact.html', {})

def portfolio(request):
	return render(request, 'portfolio.html', {})

def services(request):
	return render(request, 'services.html', {})

def single_blog(request):
	return render(request, 'single-blog.html', {})

def send_mail(request):
	mail = request.POST['nl-email']
	s = EmailMessage('new subscriber', f'{mail} has just subscribed', 'odadaxon99@gmail.com', ['khasanboevbobur@gmail.com', ])
	s.send()
	return redirect('index')