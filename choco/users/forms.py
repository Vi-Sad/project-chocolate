from django import forms
from .models import *
import random


def is_valid_password(password):
    if len(password) >= 8 and not password.isalpha() and password.isascii():
        return True
    else:
        return False


def is_valid_email(email):
    all_email = ['@yandex.ru', '@gmail.com', '@mail.ru']
    for i in all_email:
        if i in email and email.isascii():
            return True
    else:
        return False


def is_valid_name(name):
    if len(name) >= 3 and name.isascii():
        return True
    else:
        return False


class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'email']
        widgets = {}


def user_url(name):
    all_signs = 'abcdefghijklmnopqrstuvwxyz0123456789'
    all_signs = list(all_signs)
    random.shuffle(all_signs)
    all_signs.insert(random.randint(1, 35), name.lower())
    hard_id_user = ''.join(all_signs)
    return hard_id_user


class FormBasket(forms.ModelForm):
    class Meta:
        model = Basket
        fields = '__all__'
        widgets = {}


class FormFeedback(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {}
