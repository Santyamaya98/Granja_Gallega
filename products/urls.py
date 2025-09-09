# Suppliers/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('products_list/', views.products_list_view, name='products_list'),
    path('add_products/', views.products_add_view, name='addproducts'),
]   