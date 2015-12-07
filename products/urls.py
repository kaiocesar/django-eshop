from django.conf.urls import url
from . import views

app_name = 'products'

urlpatterns = [
	url(r'^$', views.index, name="home"),
	url(r'^(?P<product_id>[0-9]+)/$', views.details, name="details"),
]