# Suppliers/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('<uuid:pk>/add_products/', views.products_add_view, name='addproducts'),
]   