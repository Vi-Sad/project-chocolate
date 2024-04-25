from django.db import models


# Create your models here.

class User(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Basket(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    product_name = models.CharField(max_length=50, default=None)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
