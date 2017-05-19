from __future__ import unicode_literals

from django.db import models

class Manufacturer(models.Model):
    pass
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField()
    description = models.TextField()
    release_date = models.DateField()
    manufacturer = models.ForeignKey(Manufacturer)
