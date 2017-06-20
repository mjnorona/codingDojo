from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 40)
    description = models.TextField()
    weight = models.IntegerField()
    price = models.DecimalField(decimal_places = 2, max_digits = 4)
    cost = models.DecimalField(decimal_places = 2,max_digits = 4)
    category = models.CharField(max_length = 40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
