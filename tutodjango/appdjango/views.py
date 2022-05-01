from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ArbreForm
from .models import Arbre
from . import models
from django import forms 

def index(request):
	submitted = False
	if request.method == "POST":
		form = ArbreForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
	else:
		form = ArbreForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, "form.html", {'form': form})