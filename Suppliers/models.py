# suppliers/models.py
import uuid
from django.db import models
from django.contrib.auth.models import User
from localflavor.es.models import ESPostalCodeField, ESIdentityCardNumberField
                                                
class SuppliersModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True)
    
    # Add the missing fields that your form references
    phone = models.CharField(max_length=15)  # Will validate in form
    address = models.CharField(max_length=255)
    zip_code = ESPostalCodeField()
    province = models.CharField(max_length=90)
    location = models.CharField(max_length=150, blank=True, null=True)
    tax_id = ESIdentityCardNumberField(blank=True, null=True)
    
    production_activity = models.CharField(max_length=200, help_text="Type of farming or production activity")
    approved = models.BooleanField(default=False)  # ✅ Admin must approve

    date_joined = models.DateTimeField(auto_now_add=True)   

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"
        ordering = ['full_name']


    def __str__(self):
        return f'- approved: {self.approved}\n- id:{self.id}\n- name: {self.full_name}\n- company: {self.company_name}\n- email: {self.email}\n- address: {self.address}\n- production_activity: {self.production_activity}\n- date_joined: {self.date_joined}\n- phone: {self.phone}\n- zip_code: {self.zip_code}\n- province: {self.province}\n- location: {self.location}\n- tax_id: {self.tax_id}\n '


