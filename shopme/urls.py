from django.contrib import admin
from django.urls import path
from . import views
#from .views import *

urlpatterns = [
    path('', views.index, name = 'shopme'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('productview', views.productview, name='productview'),
    path('tracker', views.tracker, name='myorder'),
    path('checkout', views.checkout, name='checkout'),
    path('accounts', views.accounts, name='accounts'),
    path('help', views.help, name='help'),
    path('purchaseperuser', views.purchaseperuser, name='purchaseperuser')
]