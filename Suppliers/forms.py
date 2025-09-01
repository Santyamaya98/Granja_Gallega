# suppliers/forms.py
from django import forms
from localflavor.es.forms import ESPostalCodeField, ESPhoneNumberField, ESProvinceSelect, ESIdentityCardField
from .models import SuppliersModel

class SuppliersForm(forms.ModelForm):
    zip_code = ESPostalCodeField(
        label="Código Postal",
        help_text="Código postal de 5 dígitos (01000-52999)"
    )
    
    phone = ESPhoneNumberField(
        label="Teléfono",
        help_text="Número de teléfono español"
    )
    
    tax_id = ESIdentityCardField(
        required=False,
        label="NIF/CIF/NIE",
        help_text="Documento de identificación fiscal"
    )
    
    class Meta:
        model = SuppliersModel
        fields = '__all__'
        exclude = ['id', 'date_joined']  # Exclude auto-generated fields
        widgets = {
            'province': ESProvinceSelect(),
        }
        labels = {
            'full_name': 'Nombre Completo',
            'company_name': 'Nombre de Empresa',
            'email': 'Correo Electrónico',
            'address': 'Dirección',
            'location': 'Localidad',
            'production_activity': 'Actividad Productiva',
        }