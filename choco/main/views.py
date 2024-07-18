from django.contrib.auth.models import User
from django.shortcuts import render
from users.models import *
from .models import *
from django.http import HttpResponse

# Create your views here.

users = User.objects
products = Product.objects.filter(new=False)
basket = Basket.objects
new_products = Product.objects.filter(new=True)
user_chocolate = UserChocolate.objects
user_orders = Orders.objects

user_cookie = None


def error_404(request, exception):
    return render(request, 'main/error_404.html', status=404)


# class MainView(ListView):
#     model = Product
#     template_name = 'main/main.html'
#     context_object_name = 'products'
#     # paginate_by = 3
#     extra_context = {'users': users.all(), 'new_products': new_products}


def main(request):
    global user_cookie
    try:
        user_cookie = request.COOKIES['hard_id']
        if users.filter(hard_id=user_cookie).exists():
            return main_user(request)
        else:
            return render(request, 'main/main.html', context={'users': users.all(), 'new_products': new_products,
                                                              'products': products})
    except KeyError:
        return render(request, 'main/main.html', context={'users': users.all(), 'new_products': new_products,
                                                          'products': products})


def main_user(request):
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        for i in users.filter(hard_id=user_cookie):
            user_active = i.name
        total = 0
        for i in basket.filter(basket=True, hard_id=user_cookie):
            total += (i.price * i.count)
        return render(request, 'main/main_user.html', context={'users': users.all(), 'products': products,
                                                               'basket': basket.filter(basket=True,
                                                                                       hard_id=user_cookie),
                                                               'total': total, 'user_hard_id': user_cookie,
                                                               'new_products': new_products,
                                                               'user_active': user_active,
                                                               'user_orders': user_orders.filter(hard_id=user_cookie)})
    else:
        return render(request, 'main/main.html', context={'users': users.all(), 'new_products': new_products,
                                                          'products': products})


def logout(request):
    global user_cookie
    user_cookie = None
    return render(request, 'users/logout.html')

