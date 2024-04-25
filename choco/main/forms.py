from django import forms
from .models import *


class FormProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {}
