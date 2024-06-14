from django.contrib.auth.models import User
from django.shortcuts import render
from users.models import *
from .models import *

# Create your views here.

users = User.objects
products = Product.objects.filter(new=False)
basket = Basket.objects
new_products = Product.objects.filter(new=True)


def error_404(request, exception):
    return render(request, 'main/error_404.html', status=404)


class MainView(ListView):
    model = Product
    template_name = 'main/main.html'
    context_object_name = 'products'
    # paginate_by = 3
    extra_context = {'users': users.all(), 'new_products': new_products}


def main_user(request, hard_id):
    global user_active
    if users.filter(hard_id=hard_id).exists():
        for i in users.filter(hard_id=hard_id):
            user_active = i.name
        total = 0
        for i in basket.filter(basket=True):
            total += (i.price * i.count)
        return render(request, 'main/main_user.html', context={'users': users.all(),
                                                               'products': products, 'user_active': user_active,
                                                               'basket': basket.filter(basket=True,
                                                                                       hard_id=hard_id),
                                                               'total': total, 'user_hard_id': hard_id,
                                                               'new_products': new_products})
    else:
        return render(request, 'main/error_404.html', status=404)
