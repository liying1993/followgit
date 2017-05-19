from __future__ import unicode_literals

from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=16,decimal_places=2,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    release_date = models.DateField(blank=True,null=True)
    manufacturer = models.ForeignKey(Manufacturer)

