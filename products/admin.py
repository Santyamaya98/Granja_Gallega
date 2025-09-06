from django.contrib import admin
from .models import SuppliersProductsModel
# Register your models here.

@admin.register(SuppliersProductsModel)
class SuppliersProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'supplier', 'price', 'stock', 'promotion', 'expiration_date', 'created_at']
    list_filter = ['promotion', 'expiration_date', 'created_at']
    search_fields = ['name', 'description', 'supplier__company_name']
    readonly_fields = ['id', 'created_at', 'updated_at']    
