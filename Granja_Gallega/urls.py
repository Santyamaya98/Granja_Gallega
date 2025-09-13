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
#app/urls.py
# urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

# Import your viewsets
from Suppliers.viewsets import SuppliersViewSet
from products.viewsets import ProductsViewSet

# Main router for top-level resources
router = routers.DefaultRouter()
router.register(r'suppliers', SuppliersViewSet, basename='suppliers')

# Nested router for the 'products' resource under 'suppliers'
suppliers_router = routers.NestedSimpleRouter(router, r'suppliers', lookup='supplier')
suppliers_router.register(r'products', ProductsViewSet, basename='supplier-products')

urlpatterns = [
    # Admin and authentication URLs
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    # API endpoints handled by the routers
    path('api/', include(router.urls)),
    path('api/', include(suppliers_router.urls)),
    
    # Web endpoints (if needed)
    path('suppliers/', include('Suppliers.urls')),
    path('suppliers/<uuid:supplier_pk>/products/', include('products.urls')),
]
