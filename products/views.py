# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from .models import Products

def index(request):
	p = Products.objects.all()
	products = {"products" : p}
	return render(request, 'products/index.html', products)


def details(request, product_id):
	product = Products.objects.get(id=product_id)
	return render(request, 'products/details.html', {'product':product})