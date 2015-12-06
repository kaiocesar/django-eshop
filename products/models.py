from __future__ import unicode_literals

from django.db import models

class Products(models.Model):

    STATUS_CHOICE = (
        (True, 'Active'),
        (False, 'Inactive')
    )

    name = models.CharField(max_length=50, verbose_name="Product name")
    description = models.TextField(verbose_name="Description")
    created_at = models.DateTimeField(verbose_name="Created at")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    amount = models.IntegerField(verbose_name="Amount")
    discount = models.IntegerField(verbose_name="Discount")
    status = models.BooleanField(verbose_name="Status", choices=STATUS_CHOICE)


class ProductPhotos(models.Model):
    photografy = models.CharField(max_length=150)
    product = models.ForeignKey(Products)


class Categories(models.Model):
    name = models.CharField(max_length=50, verbose_name="Category name")


class CategoriesProducts(models.Model):
    product = models.ForeignKey(Products, verbose_name="Product code")
    category = models.ForeignKey(Categories, verbose_name="Category code")