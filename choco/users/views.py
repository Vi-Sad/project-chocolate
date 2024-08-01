from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
import json
from django.views.decorators.http import require_http_methods

from main.models import *
from main.views import *
from .models import *
from .forms import *
from datetime import datetime
import choco.settings as settings

import time

# Create your views here.

users = User.objects
products = Product.objects
basket = Basket.objects
feedbacks = Feedback.objects
user_chocolate = UserChocolate.objects
user_orders = Orders.objects

user_hard_id = None
user_cookie = None
url_cookie = None
start_url = 'http://127.0.0.1:8000/'


class Registration(CreateView):
    form_class = FormRegistration
    template_name = 'users/registration.html'
    extra_context = {'form': form_class}


def registration_check(request):
    form_class = FormRegistration
    name = request.POST['username']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password1']
    password_2 = request.POST['password2']
    if len(name) == 0 or len(email) == 0 or len(password) == 0:
        message = 'Поля не могут быть пустыми'
    elif all([x.email != email for x in users.all()]):
        if is_valid_password(password, password_2) and is_valid_email(email) and is_valid_name(name, lastname):
            hard_id = user_url(name)
            User.objects.create(name=name, lastname=lastname, email=email, password=password,
                                date_registration=datetime.now(), hard_id=hard_id)
            message = 'Вы успешны зарегистрированы. Попробуйте войти'
        else:
            message = 'Ваша эл. почта, никнейм или пароль не соответствуют требованиям'
    else:
        message = 'Почта уже используется'
    return render(request, 'users/registration.html', context={'message': message, 'start_url': start_url,
                                                               'form': form_class})


class Login(LoginView):
    form_class = FormLogin
    template_name = 'users/login.html'
    extra_context = {'form': form_class}


def login_check(request):
    global user_hard_id
    form_class = FormLogin
    login = request.POST['username']
    password = request.POST['password']
    if len(login) == 0 or len(password) == 0:
        message = 'Поля не могут быть пустыми'
    elif any((x.email == login or x.name == login) and x.password == password for x in users.all()):
        for i in users.all():
            if (i.email == login or i.name == login) and i.password == password:
                user_hard_id = i.hard_id
        message = 'Авторизация прошла успешно. Нажмите на кнопку "Войти" еще раз'
        response = render(request, 'users/login.html',
                          context={'message': message, 'start_url': start_url, 'form': form_class})
        response.set_cookie('hard_id', user_hard_id, secure=True, samesite='Lax', httponly=True, max_age=None)
        return response
    else:
        message = 'Не верный логин или пароль'
    return render(request, 'users/login.html', context={'message': message, 'start_url': start_url, 'form': form_class})


def logout(request):
    global user_hard_id
    user_hard_id = None
    response = render(request, 'users/logout.html')
    response.set_cookie('hard_id', user_hard_id)
    return response


# class AccountView(DetailView):
#     model = User
#     queryset = User.objects.all()
#     template_name = 'users/account.html'
#     context_object_name = 'user'
#     slug_field = 'hard_id'
#     slug_url_kwarg = 'hard_id'

def account(request):
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        return render(request, 'users/account.html', context={'user': users.filter(hard_id=user_cookie)})
    else:
        return render(request, 'main/error_404.html', status=404)


def info_product(request, id):
    global user_cookie, url_cookie
    divider = 0
    score_all_users = 0
    total = 0
    try:
        user_cookie = request.COOKIES['hard_id']
    except KeyError:
        user_cookie = None
    if products.filter(id=id).exists():
        for i in basket.filter(basket=True, hard_id=user_cookie):
            total += (i.price * i.count)
        for i in feedbacks.filter(id_product=id):
            divider += 1
            score_all_users += i.score
        if divider == 0:
            general_assessment = 0
        else:
            general_assessment = round(score_all_users / divider, 1)
        url_cookie = request.build_absolute_uri()
        response = render(request, 'main/info_product.html', context={'products': products.filter(id=id),
                                                                      'feedbacks': feedbacks.filter(id_product=id),
                                                                      'id_product': id, 'start_url': start_url,
                                                                      'user_hard_id': user_cookie,
                                                                      'general_assessment': general_assessment,
                                                                      'count_feedbacks': divider, 'users': users.all(),
                                                                      'basket': basket.filter(basket=True,
                                                                                              hard_id=user_cookie),
                                                                      'total': total, 'favourites': basket.filter(
                hard_id=user_cookie, favourites=True, id_product=id).exists()})
        response.set_cookie('url', url_cookie, secure=True, samesite='Lax', httponly=True, max_age=None)
        return response
    else:
        return render(request, 'main/error_404.html', status=404)


def view_favourites(request):
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        return render(request, 'users/favourites.html',
                      context={'favourites': basket.filter(favourites=True, hard_id=user_cookie),
                               'products': products.all(), 'user_hard_id': user_cookie})
    else:
        return render(request, 'main/error_404.html', status=404)


def view_basket(request):
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        return render(request, 'users/basket.html',
                      context={'basket': basket.filter(basket=True, hard_id=user_cookie),
                               'products': products.all(),
                               'start_url': start_url, 'user_hard_id': user_cookie,
                               'user_chocolate': user_chocolate.filter(hard_id=user_cookie)})
    else:
        return render(request, 'main/error_404.html', status=404)


def add_basket(request, id):
    global url_cookie
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        url_cookie = None
        count_product = request.POST.get('count_product')
        existence = basket.filter(id_product=id, hard_id=user_cookie, create_chocolate_user=False).exists()
        if count_product == '':
            print('Ошибка добавления')
        else:
            if not existence:
                for i in products.filter(id=id):
                    basket.create(id_product=id, count=count_product, product_name=i.product_name,
                                  favourites=False, basket=True, price=i.price, hard_id=user_cookie)
            else:
                for i in products.filter(id=id):
                    if basket.filter(id_product=id, basket=False, hard_id=user_cookie, favourites=True).exists():
                        basket.filter(id_product=id, basket=False, hard_id=user_cookie).update(price=i.price,
                                                                                               count=count_product,
                                                                                               basket=True)
                    else:
                        basket.filter(id_product=id, basket=True, hard_id=user_cookie).update(price=i.price,
                                                                                              count=count_product)
        time.sleep(1)
        return info_product(request, id)
    else:
        return render(request, 'main/error_404.html', status=404)


def delete_basket(request, id):
    user_cookie = request.COOKIES['hard_id']
    if basket.filter(id=id, hard_id=user_cookie, basket=True, favourites=True).exists():
        basket.filter(id=id, hard_id=user_cookie, basket=True, favourites=True).update(basket=False)
    else:
        basket.filter(id=id, hard_id=user_cookie, basket=True).delete()
    user_chocolate.filter(id_basket=id, hard_id=user_cookie).delete()
    return render(request, 'users/basket.html', context={'basket': basket.filter(basket=True, hard_id=user_cookie),
                                                         'products': products.all(), 'start_url': start_url,
                                                         'user_hard_id': user_cookie,
                                                         'user_chocolate': user_chocolate.filter(hard_id=user_cookie)})


def ajax_delete_basket(request, id):
    url_active = request.COOKIES['url']
    try:
        user_cookie = request.COOKIES['hard_id']
        if basket.filter(id=id, hard_id=user_cookie, basket=True, favourites=True).exists():
            basket.filter(id=id, hard_id=user_cookie, basket=True, favourites=True).update(basket=False)
        else:
            basket.filter(id=id, hard_id=user_cookie, basket=True).delete()
        user_chocolate.filter(id_basket=id, hard_id=user_cookie).delete()
        return info_product(request, url_active[(url_active.index('%3D') + 3):-1])
    except:
        return main_user(request)


def delete_favourites(request, id):
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        if basket.filter(id=id, hard_id=user_cookie, favourites=True, basket=True).exists():
            basket.filter(id=id, hard_id=user_cookie, favourites=True, basket=True).update(favourites=False)
        else:
            basket.filter(id=id, hard_id=user_cookie, favourites=True).delete()
        return render(request, 'users/favourites.html', context={'favourites': basket.filter(favourites=True,
                                                                                             hard_id=user_cookie),
                                                                 'products': products.all(),
                                                                 'user_hard_id': user_cookie})
    else:
        return render(request, 'main/error_404.html', status=404)


def delete_favourites_2(request, id_product):
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        if basket.filter(id_product=id_product, hard_id=user_cookie, favourites=True, basket=True).exists():
            basket.filter(id_product=id_product, hard_id=user_cookie, favourites=True, basket=True).update(
                favourites=False)
        else:
            basket.filter(id_product=id_product, hard_id=user_cookie, favourites=True).delete()
        return info_product(request, id_product)
    else:
        return render(request, 'main/error_404.html', status=404)


def add_favourites(request, id):
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        count_product = request.POST.get('count_product')
        if count_product == '':
            print('Ошибка добавления')
        else:
            if basket.filter(id_product=id, favourites=True, hard_id=user_cookie).exists():
                print('Ошибка добавления')
            elif basket.filter(id_product=id, favourites=False, hard_id=user_cookie, basket=True).exists():
                basket.filter(id_product=id, favourites=False, hard_id=user_cookie, basket=True).update(favourites=True)
            else:
                for i in products.filter(id=id):
                    basket.create(id_product=id, count=count_product, product_name=i.product_name,
                                  favourites=True, basket=False, hard_id=user_cookie)
        return info_product(request, id)
    else:
        return render(request, 'main/error_404.html', status=404)


def send_feedback(request, id):
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        message = request.POST.get('message')
        anonim = request.POST.get('anonim')
        score = request.POST.get('score')
        existence = feedbacks.filter(id_product=id, hard_id=user_cookie).exists()
        anonim = True if anonim == 'on' else False
        if not existence:
            feedbacks.create(id_product=id, message=message, score=score, anonim=anonim, date=datetime.now(),
                             hard_id=user_cookie)
            message = 'Спасибо за отзыв!'
        else:
            user_message = ' (изменено) '
            feedbacks.filter(id_product=id, hard_id=user_cookie).update(message=message + user_message, score=score,
                                                                        anonim=anonim, date=datetime.now())
            message = 'Отзыв обновлен. Спасибо!'
        return render(request, 'users/check_feedback.html', context={'message': message, 'start_url': start_url,
                                                                     'user_hard_id': user_cookie})
    else:
        return render(request, 'main/error_404.html', status=404)


def account_delete(request):
    global user_hard_id
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        users.filter(hard_id=user_cookie).delete()
        basket.filter(hard_id=user_cookie).delete()
        feedbacks.filter(hard_id=user_cookie).delete()
        user_hard_id, user_cookie = None, None
        response = render(request, 'users/account_delete.html')
        response.set_cookie('hard_id', user_hard_id, secure=True, samesite='Lax', httponly=True, max_age=None)
        return response
    else:
        return render(request, 'main/error_404.html', status=404)


def new_password(request):
    return render(request, 'users/new_password.html')


def new_password_check(request):
    email = request.POST.get('email')
    if users.filter(email=email).exists():
        message = 'Проверьте Вашу эл. почту'
        for i in users.filter(email=email):
            url = f'{start_url}/user/update_password/{i.hard_id}'
        send_mail('Восстановление пароля', f'Перейдите по ссылке для восстановления аккаунта.\nСсылка -> {url}',
                  settings.EMAIL_HOST_USER, [email])
    else:
        message = 'Упс! Что-то пошло не так'
    return render(request, 'users/new_password_check.html', context={'message': message})


def update_password(request, hard_id):
    # user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=hard_id).exists():
        return render(request, 'users/update_password.html', context={'hard_id': hard_id})
    else:
        return render(request, 'main/error_404.html', status=404)


def update_password_check(request, hard_id):
    # user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=hard_id).exists():
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if is_valid_password(password_1, password_2):
            message = 'Ваш пароль был успешно обновлен'
            users.filter(hard_id=hard_id).update(password=password_1)
        else:
            message = 'Пароль не соответствует требованиям'
        return render(request, 'users/update_password_check.html', context={'message': message, 'hard_id': hard_id})
    else:
        return render(request, 'main/error_404.html', status=404)


def change_password(request):
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        return render(request, 'users/change_password.html')
    else:
        return render(request, 'main/error_404.html', status=404)


def change_password_check(request):
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        password_0 = request.POST.get('password_0')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if users.filter(hard_id=user_cookie, password=password_0).exists():
            if is_valid_password(password_1, password_2) and password_0 != password_1:
                message = 'Ваш пароль был успешно изменен'
                users.filter(hard_id=user_cookie).update(password=password_1)
            elif is_valid_password(password_1, password_2) and password_0 == password_1:
                message = 'Новый пароль не должен совпадать со старым'
            else:
                message = 'Новые пароли не совпадают'
        else:
            message = 'Текущий пароль введен не верно'
        return render(request, 'users/change_password_check.html', context={'hard_id': user_cookie, 'message': message})
    else:
        return render(request, 'main/error_404.html', status=404)


def cookie_set(request):
    response = HttpResponse('Собираем куки...')
    response.set_cookie('hard_id', user_hard_id)
    return response


def cookie_get(request):
    hard_id = request.COOKIES['hard_id']
    return HttpResponse(f'Последний визит пользователя с ID: {hard_id}')


def create_chocolate(request):
    total = 0
    try:
        user_cookie = request.COOKIES['hard_id']
        for i in basket.filter(basket=True, hard_id=user_cookie):
            total += (i.price * i.count)
    except KeyError:
        user_cookie = None
    return render(request, 'users/create_chocolate.html', context={'user_hard_id': user_cookie,
                                                                   'basket': basket.filter(basket=True,
                                                                                           hard_id=user_cookie),
                                                                   'total': total})


def create_chocolate_check(request):
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        total = 0
        for i in basket.filter(basket=True, hard_id=user_cookie):
            total += (i.price * i.count)

        chocolate = request.POST.get('chocolate')
        basic = request.POST.get('basic')

        raspberry = request.POST.get('raspberry')
        pineapple = request.POST.get('pineapple')
        strawberry = request.POST.get('strawberry')
        nuts = request.POST.get('nuts')
        all_additives = [raspberry, pineapple, strawberry, nuts]
        additives = ''
        if all([x == None for x in all_additives]):
            additives = None
        else:
            for i in all_additives:
                if i != None:
                    additives += f'{i}, '
            additives = additives[:-2]

        count = request.POST.get('count')
        res_price_2 = request.POST.get('res_price_2')
        user_chocolate.create(hard_id=user_cookie, chocolate=chocolate, basic=basic,
                              additives=additives, price=res_price_2,
                              product_name='Особый шоколад 0', count=count)
        for i in user_chocolate.filter(hard_id=user_cookie, product_name='Особый шоколад 0'):
            id_product = i.id
        basket.create(hard_id=user_cookie, price=int(res_price_2) / int(count), count=count, basket=True,
                      product_name=f'Особый шоколад {id_product}', id_product=id_product, create_chocolate_user=True)
        for i in basket.filter(hard_id=user_cookie, product_name=f'Особый шоколад {id_product}'):
            id_basket = i.id
        user_chocolate.filter(hard_id=user_cookie, product_name='Особый шоколад 0').update(
            product_name=f'Особый шоколад {id_product}', id_basket=id_basket)
        time.sleep(1)
        return render(request, 'users/create_chocolate.html', context={'user_hard_id': user_cookie,
                                                                       'basket': basket.filter(basket=True,
                                                                                               hard_id=user_cookie),
                                                                       'total': total})
    else:
        return render(request, 'main/error_404.html', status=404)


def orders(request):
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        return render(request, 'users/orders.html', context={'user_orders': user_orders.filter(hard_id=user_cookie),
                                                             'user_cookie': user_cookie})
    else:
        return render(request, 'main/error_404.html', status=404)


def orders_check(request):
    user_cookie = request.COOKIES['hard_id']
    if users.filter(hard_id=user_cookie).exists():
        for i in basket.filter(hard_id=user_cookie, basket=True):
            user_orders.create(hard_id=user_cookie, id_product=i.id_product, count=i.count,
                               price=int(i.price) * int(i.count), product_name=i.product_name, status='Не готов')
            if i.favourites == True:
                basket.filter(hard_id=user_cookie, basket=True).update(basket=False)
            else:
                basket.filter(hard_id=user_cookie, basket=True).delete()
        return render(request, 'users/orders_check.html', context={'user_orders': user_orders.filter(
            hard_id=user_cookie), 'user_cookie': user_cookie})
    else:
        return render(request, 'main/error_404.html', status=404)
