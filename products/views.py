# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from .models import Products

def index(request):
	p = Products.objects.all()
	products = {"products" : p}
	return render(request, 'products/index.html', products)
