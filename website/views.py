from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Home page")

def about(request):
	return HttpResponse("About")

def contact(request):
	return HttpResponse("Contact")

def register_costumers(request):
	return HttpResponse("Register costumers")