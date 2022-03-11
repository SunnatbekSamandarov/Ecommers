from django.contrib import admin
from django.urls import path
from .views import  index,product_view

urlpatterns = [
    path('', index,name = 'home'),
    path('product/',product_view,name='product')
]
