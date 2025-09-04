# suppliers/forms.py
from django import forms
from django.core.validators import RegexValidator
from localflavor.es.forms import ESPostalCodeField,  ESProvinceSelect, ESIdentityCardNumberField
from .models import SuppliersModel
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

phone_validator = RegexValidator(
    regex=r'^\+?34?\d{9}$',  # Spanish phone numbers (+34 optional, 9 digits)
    message="Enter a valid Spanish phone number (e.g. +34911123456 or 911123456)."
)


class SuppliersForm(forms.ModelForm):
    zip_code = ESPostalCodeField(
        label="Código Postal",
        help_text="Código postal de 5 dígitos (01000-52999)"
    )

    phone = forms.CharField(
        label="Teléfono",
        max_length=15,
        validators=[phone_validator]
    )

    tax_id = ESIdentityCardNumberField(
        required=True,
        label="NIF/CIF/NIE",
        help_text="Documento de identificación fiscal"
    )
    
    class Meta:
        model = SuppliersModel
        fields = '__all__'
        exclude = ['id', 'date_joined', 'user']  # Exclude auto-generated fields
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

class SuppliersSignupForm(forms.Form):
    token_id = forms.UUIDField(label="Token de Validación")
    username = forms.CharField(label="Nombre de Usuario", required=True)
    email = forms.EmailField(label="Correo Electrónico", required=True)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            raise ValidationError("Las contraseñas no coinciden.")
        return cleaned_data
    
class SupplierLoginForm(forms.Form):
    username = forms.CharField(label="Nombre de Usuario", required=True)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label="Recuérdame", required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Nombre de usuario o contraseña incorrectos.")
            if not user.is_active:
                raise forms.ValidationError("Esta cuenta está inactiva.")
        return cleaned_data