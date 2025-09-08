from rest_framework import serializers
from .models import SuppliersModel

class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuppliersModel
        fields = [
                'id',
                'approved',
                'date_joined',
                'user',
                'tax_id',
                'company_name',
                'full_name',
                'email',
                'phone',
                'address',
                'zip_code',
                'province',
                'location',
                'production_activity',
                ]  
