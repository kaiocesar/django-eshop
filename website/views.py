# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products

def index(request):
	return render(request, 'website/index.html')

def about(request):
	return render(request, 'website/about.html')

def contact(request):
	return render(request, 'website/contact.html')

def register_costumers(request):
	return render(request, 'website/register.html')