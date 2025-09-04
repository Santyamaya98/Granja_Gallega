"""
URL configuration for Granja_Gallega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Suppliers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Suppliers_View, name='suppliers'),
    path('list/', views.Suppliers_List, name='supplier_list'),
    path('signup/', views.Suppliers_Sign_Up_View, name='suppliers_signup'),
    path('create/', views.supplier_create, name='supplier_create'),
    path('login/', views.Suppliers_Login_View, name='Login'),
    path('logout/', views.Suppliers_Logout_View, name='Logout'),
    path('dashboard/', views.Suppliers_Dashboard_View, name='Dashboard'),
    path('<uuid:pk>/', views.supplier_detail, name='supplier_detail'),
    path('<uuid:pk>/edit/', views.supplier_edit, name='supplier_edit'),
    path('<uuid:pk>/delete/', views.supplier_delete, name='supplier_delete'),
]