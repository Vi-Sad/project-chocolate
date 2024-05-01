from django.contrib.auth.models import User
from django.shortcuts import render
from users.models import *
from .models import *

# Create your views here.

users = User.objects.all()
products = Product.objects.all()
basket = Basket.objects


def main(request):
    return render(request, 'main/main.html', context={'users': users, 'products': products, 'basket': basket.all()})


def main_user(request, name):
    return render(request, 'main/main_user.html', context={'user_active': name, 'users': users, 'products': products,
                                                           'basket': basket.filter(name=name)})

