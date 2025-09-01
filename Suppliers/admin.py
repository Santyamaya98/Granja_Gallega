from django.contrib import admin
from .models import SuppliersModel

@admin.register(SuppliersModel)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'company_name', 'email', 'phone', 'province', 'date_joined']
    list_filter = ['province', 'date_joined']
    search_fields = ['full_name', 'company_name', 'email']
    readonly_fields = ['id', 'date_joined']