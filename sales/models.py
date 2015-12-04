from __future__ import unicode_literals

from django.db import models


class PaymentsMethods(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Sales(models.Model):
    code = models.CharField(max_length='40', verbose_name="Code sales")
    status = models.CharField(max_length='50', verbose_name="Status")
    payment_method = models.ForeignKey(PaymentsMethods, verbose_name="Payment Method")
    customer = models.ForeignKey('customers.Customers', "Customer")



class SaleProducts(models.Model):
    product = models.ForeignKey('products.Products', verbose_name="Product code")
    sales = models.ForeignKey(Sales, verbose_name="Sales code")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    amount = models.IntegerField()
    discount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)




