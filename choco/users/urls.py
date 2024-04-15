from django.urls import path, re_path

import users.views as users

urlpatterns = [
    path('registration/', users.registration, name='registration'),
    path('registration/check/', users.registration_check, name='registration_check'),
    path('login/', users.login, name='login'),
    path('login/check', users.login_check, name='login_check'),
]
