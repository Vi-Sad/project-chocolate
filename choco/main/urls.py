from django.urls import path, re_path

import main.views as main

urlpatterns = [
    path('', main.main, name='main'),
]
