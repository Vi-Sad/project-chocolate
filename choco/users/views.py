from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail

from main.models import *
from .models import *
from .forms import *
from datetime import datetime
import choco.settings as settings

# Create your views here.

users = User.objects
products = Product.objects
basket = Basket.objects
feedbacks = Feedback.objects

user_active, user_hard_id = None, None
start_url = 'http://127.0.0.1:8000/'


class Registration(CreateView):
    form_class = FormRegistration
    template_name = 'users/registration.html'


def registration_check(request):
    name = request.POST['username']
    email = request.POST['email']
    password = request.POST['password1']
    password_2 = request.POST['password2']
    if len(name) == 0 or len(email) == 0 or len(password) == 0:
        message = 'Поля не могут быть пустыми'
        url = 'registration'
    elif all([x.name != name or x.email != email for x in users.all()]):
        if is_valid_password(password, password_2) and is_valid_email(email) and is_valid_name(name):
            hard_id = user_url(name)
            User.objects.create(name=name, email=email, password=password, date_registration=datetime.now(),
                                hard_id=hard_id)
            url = 'main'
            message = 'Вы успешны зарегистрированы. Попробуйте войти'
        else:
            url = 'registration'
            message = 'Ваша эл. почта, никнейм или пароль не соответствуют требованиям'
    else:
        message = 'Почта уже используется'
        url = 'registration'
    return render(request, 'users/registration_check.html', context={'message': message, 'url': url})


class Login(LoginView):
    form_class = FormLogin
    template_name = 'users/login.html'
    extra_context = {'form': form_class}


def login_check(request):
    global user_active, user_hard_id
    login = request.POST['username']
    password = request.POST['password']
    if len(login) == 0 or len(password) == 0:
        message = 'Поля не могут быть пустыми'
        url = 'user/login/'
    elif any((x.email == login or x.name == login) and x.password == password for x in users.all()):
        for i in users.all():
            if (i.email == login or i.name == login) and i.password == password:
                user_active, user_hard_id = i.name, i.hard_id
        message = 'Вы успешно вошли'
        url = f'{start_url}/user_active/{user_active}/{user_hard_id}/'
    else:
        url = f'{start_url}/user/login/'
        message = 'Не верный логин или пароль'
    return render(request, 'users/login_check.html', context={'message': message, 'url': url, 'start_url': start_url})


class AccountView(DetailView):
    model = User
    queryset = User.objects.all()
    template_name = 'users/account.html'
    context_object_name = 'user'
    slug_field = 'hard_id'
    slug_url_kwarg = 'hard_id'


def info_product(request, id):
    return render(request, 'main/info_product.html',
                  context={'products': products.filter(id=id), 'user_active': user_active,
                           'feedbacks': feedbacks.filter(id_product=id), 'id': id, 'start_url': start_url,
                           'user_hard_id': user_hard_id})


def view_favourites(request, name, hard_id):
    if users.filter(hard_id=hard_id, name=name).exists():
        return render(request, 'users/favourites.html',
                      context={'favourites': basket.filter(name=name, favourites=True, hard_id=hard_id),
                               'user_active': name, 'products': products.all(), 'user_hard_id': hard_id})
    else:
        return render(request, 'main/error_404.html', status=404)


def view_basket(request, name, hard_id):
    if users.filter(hard_id=hard_id, name=name).exists():
        return render(request, 'users/basket.html',
                      context={'basket': basket.filter(name=name, basket=True, hard_id=hard_id),
                               'user_active': name, 'products': products.all(),
                               'start_url': start_url, 'user_hard_id': hard_id})
    else:
        return render(request, 'main/error_404.html', status=404)


def add_basket(request, name, id, hard_id):
    count_product = request.POST.get('count_product')
    existence = basket.filter(id_product=id, name=name, hard_id=hard_id).exists()
    if count_product == '':
        message = 'Упс! Что-то пошло не так'
    else:
        if not existence:
            for i in products.filter(id=id):
                basket.create(name=name, id_product=id, count=count_product, product_name=i.product_name,
                              favourites=False, basket=True, price=i.price, hard_id=hard_id)
            message = 'Товар успешно добавлен в корзину'
        else:
            if basket.filter(id_product=id, favourites=True, name=name, hard_id=hard_id).exists():
                basket.filter(id_product=id, hard_id=hard_id).update(basket=True)
                message = 'Товар успешно добавлен в корзину'
            else:
                message = 'Товар уже есть в корзине'
    return render(request, 'users/add_basket.html', context={'user_active': user_active, 'message': message,
                                                             'user_hard_id': hard_id})


def delete_basket(request, name, id, hard_id):
    basket.filter(id=id, name=name, hard_id=hard_id).delete()
    return render(request, 'users/delete_basket.html', context={'user_active': user_active, 'user_hard_id': hard_id})


def add_favourites(request, name, id, hard_id):
    count_product = request.POST.get('count_product')
    existence = basket.filter(name=name, id_product=id, hard_id=hard_id).exists()
    if count_product == '':
        message = 'Упс! Что-то пошло не так'
    else:
        if basket.filter(name=name, id_product=id, favourites=True, hard_id=hard_id).exists():
            message = 'Товар уже есть в Избранном'
        elif existence:
            basket.filter(id_product=id, hard_id=hard_id).update(favourites=True)
            message = 'Товар успешно добавлен в Избранное'
        else:
            for i in products.filter(id=id):
                basket.create(name=name, id_product=id, count=count_product, product_name=i.product_name,
                              favourites=True, basket=False, hard_id=hard_id)
            message = 'Товар успешно добавлен в Избранное'
    return render(request, 'users/add_favourites.html', context={'user_active': user_active, 'message': message,
                                                                 'user_hard_id': hard_id})


def send_feedback(request, name, id, hard_id):
    score = request.POST.get('score')
    message = request.POST.get('message')
    anonim = request.POST.get('anonim')
    existence = feedbacks.filter(name=name, id_product=id, hard_id=hard_id).exists()
    anonim = True if anonim == 'on' else False
    if not existence:
        feedbacks.create(name=name, id_product=id, message=message, score=score, anonim=anonim, date=datetime.now(),
                         hard_id=hard_id)
        message = 'Спасибо за отзыв!'
    else:
        user_message = ' (изменено) '
        feedbacks.filter(name=name, id_product=id, hard_id=hard_id).update(message=message + user_message, score=score,
                                                                           anonim=anonim, date=datetime.now())
        message = 'Отзыв обновлен. Спасибо!'
    return render(request, 'users/check_feedback.html', context={'user_active': user_active, 'message': message,
                                                                 'start_url': start_url, 'user_hard_id': hard_id})


def account_delete(request, name, hard_id):
    global user_active, user_hard_id
    users.filter(name=name, hard_id=hard_id).delete()
    basket.filter(name=name, hard_id=hard_id).delete()
    feedbacks.filter(name=name, hard_id=hard_id).delete()
    user_active, user_hard_id = None, None
    return render(request, 'users/account_delete.html')


def new_password(request):
    return render(request, 'users/new_password.html')


def new_password_check(request):
    email = request.POST.get('email')
    if users.filter(email=email).exists():
        message = 'Проверьте Вашу эл. почту'
        for i in users.filter(email=email):
            url = f'{start_url}/user/update_password/{i.hard_id}/'
        send_mail('Восстановление пароля', f'Перейдите по ссылке для восстановления аккаунта.\nСсылка -> {url}',
                  settings.EMAIL_HOST_USER, [email])
    else:
        message = 'Упс! Что-то пошло не так'
    return render(request, 'users/new_password_check.html', context={'message': message})


def update_password(request, hard_id):
    if users.filter(hard_id=hard_id).exists():
        return render(request, 'users/update_password.html', context={'hard_id': hard_id})
    else:
        return render(request, 'main/error_404.html', status=404)


def update_password_check(request, hard_id):
    if users.filter(hard_id=hard_id).exists():
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if is_valid_password(password_1, password_2):
            message = 'Ваш пароль был успешно обновлен'
            users.filter(hard_id=hard_id).update(password=password_1)
        else:
            message = 'Пароль не соответствует требованиям'
        return render(request, 'users/update_password_check.html', context={'message': message})
    else:
        return render(request, 'main/error_404.html', status=404)


def change_password(request, hard_id):
    if users.filter(hard_id=hard_id).exists():
        return render(request, 'users/change_password.html', context={'hard_id': hard_id})
    else:
        return render(request, 'main/error_404.html', status=404)


def change_password_check(request, hard_id):
    if users.filter(hard_id=hard_id).exists():
        password_0 = request.POST.get('password_0')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if users.filter(hard_id=hard_id, password=password_0).exists():
            if is_valid_password(password_1, password_2):
                message = 'Ваш пароль был успешно изменен'
                users.filter(hard_id=hard_id).update(password=password_1)
            else:
                message = 'Новые пароли не совпадают'
        else:
            message = 'Текущий пароль введен не верно'
        return render(request, 'users/change_password_check.html', context={'hard_id': hard_id, 'message': message})
    else:
        return render(request, 'main/error_404.html', status=404)
