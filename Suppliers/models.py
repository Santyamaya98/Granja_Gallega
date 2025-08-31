from django.db import models

# Create your models here.
class Suppliers(models.Model):
    title = models.TextField(max_length = 80),
