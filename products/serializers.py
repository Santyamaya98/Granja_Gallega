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
        
class ProdcutsPromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuppliersProductsModel
        fields = ['description',
                'start_promo_date',
                'end_promo_date',
                'price',
                'stock',   
                ]

        
