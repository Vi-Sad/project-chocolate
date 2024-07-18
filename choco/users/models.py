from django.db import models
from main.models import *


# Create your models here.

class User(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30, default=None)
    email = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=20)
    date_registration = models.DateField(default=None)
    hard_id = models.CharField(default=None, unique=True, max_length=50)

    def __str__(self):
        return self.name


class Basket(models.Model):
    objects = None
    hard_id = models.CharField(default=None, max_length=50)
    id_product = models.IntegerField(default=0)
    product_name = models.CharField(max_length=50, default=None)
    count = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    favourites = models.BooleanField(default=False)
    basket = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name


class Orders(models.Model):
    objects = None
    hard_id = models.CharField(default=None, max_length=50)
    id_product = models.IntegerField(default=0)
    product_name = models.CharField(max_length=50, default=None)
    count = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    status = models.CharField(default=None, max_length=50)

    def __str__(self):
        return self.hard_id


class UserChocolate(models.Model):
    objects = None
    product_name = models.CharField(max_length=50, default=None)
    chocolate = models.CharField(default=None, max_length=50)
    basic = models.CharField(default=None, max_length=50)
    additives = models.CharField(default=None, max_length=50, null=True)
    hard_id = models.CharField(default=None, max_length=50)
    count = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    id_basket = models.IntegerField(default=0)

    def __str__(self):
        return self.hard_id


class Feedback(models.Model):
    objects = None
    hard_id = models.CharField(default=None, max_length=50)
    score = models.IntegerField()
    message = models.CharField(max_length=2000, default=None)
    id_product = models.IntegerField(default=0)
    anonim = models.BooleanField(default=False)
    date = models.DateField(default=None)

    def __str__(self):
        return self.message
