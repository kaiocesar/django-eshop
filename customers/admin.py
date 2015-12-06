from django.contrib import admin
from customers.models import Customers

class CustomersAdmin(admin.ModelAdmin):
	pass

admin.site.register(Customers, CustomersAdmin)