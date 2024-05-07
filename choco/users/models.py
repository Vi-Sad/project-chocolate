from django.db import models
from main.models import *


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
    name = models.CharField(max_length=20, default=None)
    id_product = models.IntegerField(default=0)
    product_name = models.CharField(max_length=50, default=None)
    count = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    favourites = models.BooleanField(default=False)
    basket = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    objects = None
    name = models.CharField(max_length=20, default=None)
    score = models.IntegerField()
    message = models.CharField(max_length=2000, default=None)
    id_product = models.IntegerField(default=0)

    def __str__(self):
        return self.name
