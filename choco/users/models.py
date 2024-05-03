from django.db import models


# Create your models here.

class User(models.Model):
    objects = None
    name = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Basket(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    id_product = models.IntegerField(default=0)
    product_name = models.CharField(max_length=50, default=None)
    count = models.IntegerField(default=1)
    favourites = models.BooleanField(default=False)
    basket = models.BooleanField(default=False)

    def __str__(self):
        return self.name
