from django.shortcuts import render
from .models import *
from main.models import *
from .forms import *
from datetime import datetime

# Create your views here.

users = User.objects.all()
products = Product.objects
basket = Basket.objects
feedbacks = Feedback.objects

user_active = None
start_url = 'http://127.0.0.1:8000/'


def registration_check(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    if len(name) == 0 or len(email) == 0 or len(password) == 0:
        message = 'Поля не могут быть пустыми'
        url = 'registration'
    elif all([x.name != name or x.email != email for x in users]):
        if is_valid_password(password) and is_valid_email(email):
            User.objects.create(name=name, email=email, password=password, date_registration=datetime.now())
            url = 'main'
            message = 'Вы успешны зарегистрированы. Попробуйте войти'
        else:
            url = 'registration'
            message = 'Ваш email или пароль не соответствуют требованиям'
    else:
        if any([x.name == name for x in users]):
            message = f'Пользователь с именем "{name}" уже занят'
        else:
            message = f'Почта уже используется'
        url = 'registration'
    return render(request, 'users/registration_check.html', context={'message': message, 'url': url})


def login_check(request):
    global user_active
    email = request.POST['email']
    password = request.POST['password']
    if len(email) == 0 or len(password) == 0:
        message = 'Поля не могут быть пустыми'
        url = 'user/login/'
    elif any(x.email == email and x.password == password for x in users):
        for i in users:
            if i.email == email and i.password == password:
                user_active = i.name
        message = 'Вы успешно вошли'
        url = f'user_active/{user_active}/'
    else:
        url = 'user/login/'
        message = 'Не верный логин или пароль'
    return render(request, 'users/login_check.html', context={'message': message, 'url': url})


def logout(request):
    global user_active
    user_active = None
    return render(request, 'users/logout.html')


def account(request, name):
    return render(request, 'users/account.html', context={'users': users, 'user_active': name})


def info_product(request, id):
    return render(request, 'main/info_product.html',
                  context={'products': products.filter(id=id), 'user_active': user_active,
                           'feedbacks': feedbacks.filter(id_product=id), 'id': id, 'start_url': start_url})


def view_favourites(request, name):
    return render(request, 'users/favourites.html',
                  context={'favourites': basket.filter(name=name, favourites=True), 'user_active': user_active,
                           'products': products.all()})


def view_basket(request, name):
    return render(request, 'users/basket.html',
                  context={'basket': basket.filter(name=name, basket=True), 'user_active': user_active,
                           'products': products.all(), 'start_url': start_url})


def add_basket(request, name, id):
    count_product = request.POST.get('count_product')
    existence = basket.filter(id_product=id, name=name).exists()
    if count_product == '':
        message = 'Упс! Что-то пошло не так'
    else:
        if not existence:
            for i in products.filter(id=id):
                basket.create(name=name, id_product=id, count=count_product, product_name=i.product_name,
                              favourites=False, basket=True, price=i.price)
            message = 'Товар успешно добавлен в корзину'
        else:
            if basket.filter(id_product=id, favourites=True, name=name).exists():
                basket.filter(id_product=id).update(basket=True)
                message = 'Товар успешно добавлен в корзину'
            else:
                message = 'Товар уже есть в корзине'
    return render(request, 'users/add_basket.html', context={'user_active': user_active, 'message': message})


def delete_basket(request, name, id):
    basket.filter(id=id, name=name).delete()
    return render(request, 'users/delete_basket.html', context={'user_active': user_active})


def add_favourites(request, name, id):
    count_product = request.POST.get('count_product')
    existence = basket.filter(name=name, id_product=id).exists()
    if count_product == '':
        message = 'Упс! Что-то пошло не так'
    else:
        if basket.filter(name=name, id_product=id, favourites=True).exists():
            message = 'Товар уже есть в Избранном'
        elif existence:
            basket.filter(id_product=id).update(favourites=True)
            message = 'Товар успешно добавлен в Избранное'
        else:
            for i in products.filter(id=id):
                basket.create(name=name, id_product=id, count=count_product, product_name=i.product_name,
                              favourites=True, basket=False)
            message = 'Товар успешно добавлен в Избранное'
    return render(request, 'users/add_favourites.html', context={'user_active': user_active, 'message': message})


def send_feedback(request, name, id):
    score = request.POST.get('score')
    message = request.POST.get('message')
    anonim = request.POST.get('anonim')
    existence = feedbacks.filter(name=name, id_product=id).exists()
    anonim = True if anonim == 'on' else False
    if not existence:
        feedbacks.create(name=name, id_product=id, message=message, score=score, anonim=anonim, date=datetime.now())
        message = 'Спасибо за отзыв!'
    else:
        feedbacks.filter(name=name, id_product=id).update(message=message, score=score, anonim=anonim,
                                                          date=datetime.now())
        message = 'Отзыв обновлен. Спасибо!'
    return render(request, 'users/check_feedback.html', context={'user_active': user_active, 'message': message,
                                                                 'start_url': start_url})
