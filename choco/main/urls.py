from django.urls import path, re_path

import main.views as main

urlpatterns = [
    path('', main.main, name='main'),
    path('user_active/<slug:name>/', main.main_user, name='main_user')
]
