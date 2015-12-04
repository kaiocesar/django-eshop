from __future__ import unicode_literals

from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    rg = models.CharField(max_length=20, verbose_name="RG")
    email = models.CharField(max_length=50, verbose_name="E-mail")
    zip_code = models.CharField(max_length=10, verbose_name="Zip code")
    address = models.CharField(max_length=60, verbose_name="Address")
    street = models.CharField(max_length=50, verbose_name="Street")
    neighborhood = models.CharField(max_length=50, verbose_name="Neighborhood")
    city = models.CharField(max_length=50, verbose_name="City")
    phone = models.CharField(max_length=12, verbose_name="Phone")
    cellphone = models.CharField(max_length=12, verbose_name="Cellphone")
    description = models.TextField(verbose_name="Description")
    avatar = models.TextField(verbose_name="Avatar")

