from django.shortcuts import render
from .models import *
from main.models import *
from .forms import *

# Create your views here.

users = User.objects.all()
products = Product.objects
user_active = None


def registration(request):
    return render(request, 'users/registration.html')


def registration_check(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    form = FormUser(request.POST)
    if len(name) == 0 or len(email) == 0 or len(password) == 0:
        message = 'Поля не могут быть пустыми'
        url = 'registration'
    elif all([x.name != name or x.email != email for x in users]) and form.is_valid():
        User.objects.create(name=name, email=email, password=password)
        message = 'Вы успешны зарегистрированы. Попробуйте войти'
        url = 'main'
    else:
        if any([x.name == name for x in users]):
            message = f'Пользователь с именем "{name}" уже занят'
        else:
            message = f'Почта уже используется другим пользователем'
        url = 'registration'
    return render(request, 'users/registration_check.html', context={'message': message, 'url': url})


def login(request):
    return render(request, 'users/login.html')


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
                  context={'products': products.filter(id=id), 'user_active': user_active})
