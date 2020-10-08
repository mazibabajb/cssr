from django.shortcuts import render
from django.contrib import messages
from.models import Contact
from.forms import regform,contactform
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request, 'teacherapp/home.html')

def about(request):
	return render(request, 'teacherapp/about.html')


def contact(request):
	if request.method == 'POST':
		form = contactform(request.POST)
		if form.is_valid():
			form.save()
			firstname = form.cleaned_data.get('firstname')
			messages.success(request, f'Thank you for contacting us')

	form = contactform()
	return render(request, 'teacherapp/contact.html', {'form': form})

def business(request):
	return render(request, 'teacherapp/business.html')		

def hospitality(request):
	return render(request, 'teacherapp/hospitality.html')

def hrm(request):
	return render(request, 'teacherapp/hrm.html')	

def accounting(request):
	return render(request, 'teacherapp/accounting.html')

def businessm(request):
	return render(request, 'teacherapp/businessm.html')		

def social(request):
	return render(request, 'teacherapp/social.html')			


def blog(request):
	return render(request, 'teacherapp/blog.html')		

def marketing(request):
	return render(request, 'teacherapp/marketing.html')		

def hac(request):
	return render(request, 'teacherapp/hac.html')		

def tourism(request):
	return render(request, 'teacherapp/tourism.html')

def register(request):
	if request.method == 'POST':
		form = regform(request.POST)
		if form.is_valid():
			form.save()
			firstname = form.cleaned_data.get('firstname')
			messages.success(request, f'Your registration is being processed')
	form = regform()
	return render(request, 'teacherapp/register.html', {'form': form})		

def admissions(request):
	return render(request, 'teacherapp/admissions.html')	

def fees(request):
	return render(request, 'teacherapp/fees.html')		


def infomation(request):
	return render(request, 'teacherapp/infomation.html')							