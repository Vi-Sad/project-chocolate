from django.db import models


# Create your models here.

class Product(models.Model):
    objects = None
    category = models.CharField(max_length=20, default=None)
    product_name = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=150, default=None)
    price = models.IntegerField(default=0)
    grams = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
