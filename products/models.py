from django.db import models
from Suppliers.models import SuppliersModel
# Create your models here.
class SuppliersProductsModel(models.Model): 
    # 1. Validate supplier by token (uuid)
    id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(SuppliersModel, on_delete=models.CASCADE, related_name="products")
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
        ordering = ['name']

    def get_id(self):
        return {'id':int(self.id)}

    def __str__(self):
        return f'- name: {self.name}\n - description: {self.description}\n- expiration_date: {self.expiration_date}\n - price: {self.price}\n - stock: {self.stock}\n - promotion: {self.promotion}'
    
