import uuid
from django.db import models

from localflavor.es.forms import ESPostalCodeField, ESPhoneNumberField, ESProvinceSelect



# Create your models here.
class SuppliersModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    full_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True)
    # spanish forms using localflavor pip install django-localflavor
    
    address = models.CharField(max_length=255)


    production_activity = models.CharField(max_length=200, help_text="Type of farming or production activity")
    date_joined = models.DateTimeField(auto_now_add=True)   

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"
        ordering = ['full_name']

    def __str__(self):
        return f'{self.id} : {self.full_name}\n- {self.company_name}\n- {self.email}\n- {self.address}\n- {self.production_activity}\n- {self.date_joined}'

    class SuppliersForm(forms.Form):
        zip_code = ESPostalCodeField(help_text="5 digitos del Código Postal")
        location = ESProvinceSelect(max_length=150)  # could later be a ForeignKey to a "Region" model
        phone = ESPhoneNumberField(help_text="Número de teléfono +34")

