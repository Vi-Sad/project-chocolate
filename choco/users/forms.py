from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *
import random


def is_valid_password(password, password_2):
    if len(password) >= 8 and not password.isalpha() and password.isascii() and password == password_2:
        return True
    else:
        return False


def is_valid_email(email):
    all_email = ['@yandex.ru', '@gmail.com']
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


class FormRegistration(UserCreationForm):
    username = forms.CharField(label='Придумайте никнейм', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Придумайте пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class FormLogin(AuthenticationForm):
    username = forms.CharField(label='Логин (эл. почта или никнейм)',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


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
