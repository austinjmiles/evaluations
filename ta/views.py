import numpy as np 
import pandas as pd 
from django.shortcuts import render
from django.core.mail import send_mail, send_mass_mail
from django.http import HttpResponse, HttpResponseRedirect
from .models import Survey, Lab, Student
from django.template import loader
from .forms import ProductForm



def index(request):
	return render(request=request, 
				template_name="ta/index.html", 
				context={})


def form(request):

	form = ProductForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		form.save()
		return HttpResponseRedirect('/ta/')

	context = {
		'form' : form

	}
	return render(request, "ta/form.html", context )

def stats(request):
	count = Survey.objects.all().count()
	results = []

	for i in range(1,count+1):
		answer = Survey.objects.get(pk=i)
		print(answer.lab)


	context ={
		
	}

	return render(request, 'ta/stats.html', context)

def email(request):

	students = Student.objects.all()
	to_emails = []
	i = 0
	for stu in students:
		to_emails.append(stu.email)
	message1 = ('TA evaluations', 'Here is a link to fill out your evaluations: http://localhost:8000/login ', 'austinjmiles@gmail.com', to_emails)
	send_mass_mail((message1,), fail_silently=False)
	context = {

	}
	return render(request, "ta/email.html", context)

def results(request):

	answers = Survey.objects.all()

	


	context = {
		'answers' : answers
	}
	return render(request, "ta/results.html",context)






























