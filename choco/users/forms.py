from django import forms

from .models import *


def is_valid_password(password):
    numbers = '1234567890'
    for i in numbers:
        if i not in password and len(password) < 8:
            return False
    else:
        return True


def is_valid_email(email):
    all_email = ['@yandex.ru', '@gmail.com', '@mail.ru']
    for i in all_email:
        if i in email:
            return True
    else:
        return False


class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'email']
        widgets = {}


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
