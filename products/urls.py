# Suppliers/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('add_products/', views.products_add_view, name='addproducts'),
]   