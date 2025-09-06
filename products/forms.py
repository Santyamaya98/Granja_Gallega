from django import forms
from .models import SuppliersProductsModel
from django.core.exceptions import ValidationError

class SuppliersProductsForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="Product Name")
    description = forms.CharField(widget=forms.Textarea, label="Product Description")   
    expiration_date = forms.DateField(widget=forms.SelectDateWidget, label="Expiration Date")
    promotion = forms.BooleanField(required=False, label="Promotion")   
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Price")
    confirm_price = forms.DecimalField(label="Confirmar Precio", max_digits=10, decimal_places=2)
    stock = forms.IntegerField(label="Stock Quantity")

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        confirm_price = cleaned_data.get('confirm_price')
        if price != confirm_price:
            raise ValidationError("El precio no coincide.")
        return cleaned_data

    class Meta:
        model = SuppliersProductsModel
        # List model fields explicitly (exclude confirm_price!)
        fields = [
            'name',
            'description',
            'expiration_date',
            'promotion',
            'price',
            'stock',
        ]
        labels = {
            'name': "Product Name",
            'description': "Product Description",
            'expiration_date': "Expiration Date",
            'promotion': "Promotion",
            'price': "Price",
            'stock': "Stock Quantity",
        }