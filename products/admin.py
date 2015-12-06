from django.contrib import admin
from products.models import Products

class ProductsAdmin(admin.ModelAdmin):
	pass

admin.site.register(Products, ProductsAdmin)