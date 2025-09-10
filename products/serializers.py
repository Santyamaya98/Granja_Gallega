from rest_framework import serializers
from .models import SuppliersProductsModel

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuppliersProductsModel
        fields = [ 'id', 
                  'supplier', 
                  'updated_at', 
                  'created_at',
                  'name', 
                  'description', 
                  'expiration_date', 
                  'promotion', 
                  'price', 
                  'stock'
                  ]
        

        
