from __future__ import unicode_literals

from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name="Product name")
    description = models.TextField(verbose_name="Description")
    created_at = models.DateTimeField(verbose_name="Created at")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")