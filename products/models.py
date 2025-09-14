from django.db import models
from Suppliers.models import SuppliersModel
# Create your models here.
class SuppliersProductsModel(models.Model): 
    # 1. Validate supplier by token (uuid)
    supplier = models.ForeignKey(SuppliersModel, on_delete=models.CASCADE, related_name="products")
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    expiration_date = models.DateField()    
    promotion = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Supplier Product"
        verbose_name_plural = "Supplier Products"
        ordering = ['id']

    def __str__(self):
        return f'- id: {self.id}\n  - name: {self.name}\n - description: {self.description}\n- expiration_date: {self.expiration_date}\n - price: {self.price}\n - stock: {self.stock}\n - promotion: {self.promotion}'
    
class PromosModel(models.Model):
    # 1. identify the product by id
    product = models.ForeignKey(SuppliersProductsModel, on_delete=models.CASCADE, related_name="promotions")
    id = models.AutoField(primary_key=True)
    description = models.CharField()
    start_promo_date = models.DateField()
    end_promo_date = models.DateField()
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = "promotion"
        verbose_name_plural = "promotions"
        ordering = ['id']

    def __str__(self):
        return f'- promo_id: {self.id}\n - {self.product}'

    