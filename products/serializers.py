from rest_framework import serializers
from .models import SuppliersProductsModel, PromosModel

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
    product_name = serializers.SerializerMethodField()
    class Meta:
        model = PromosModel
        fields = [  'id',
                    'product',
                    'product_name',
                    'description',
                    'start_promo_date',
                    'end_promo_date',
                    'price',
                    'stock',   
                ]
    def get_product_name(self, obj):
        return obj.product.name  # accesses the FK's name field

        