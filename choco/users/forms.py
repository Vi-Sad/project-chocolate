from django import forms
from .models import *


class FormUser(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['name', 'password', 'email']
        widgets = {}


class FormBasket(forms.ModelForm):
    class Meta:
        model = Basket
        fields = '__all__'
        widgets = {}

