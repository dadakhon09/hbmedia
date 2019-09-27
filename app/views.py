from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

def index(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def contact(request):
	full_name = request.POST.get('full-name')
	email = request.POST.get('email')
	organization = request.POST.get('organization')
	phone = request.POST.get('phone')
	message = request.POST.get('message')

	m = EmailMessage('contact request', f'From: {full_name}\n Email: {email}\n Organization: {organization}\n Phone: {phone}\n Message:\n{message}\n', 'odadaxon99@gmail.com', ['khasanboevbobur@gmail.com', ])
	m.send()
	return render(request, 'contact.html', {})

def portfolio(request):
	return render(request, 'portfolio.html', {})

def services(request):
	return render(request, 'services.html', {})

def single_blog(request):
	return render(request, 'single-blog.html', {})

def send_mail(request):
	mail = request.POST.get('nl-email')
	s = EmailMessage('new subscriber', f'{mail} has just subscribed', 'odadaxon99@gmail.com', ['khasanboevbobur@gmail.com', ])
	s.send()
	return redirect('index')