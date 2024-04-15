from django.shortcuts import render
from users.models import User

# Create your views here.

users = User.objects.all()


def main(request):
    return render(request, 'main/main.html', context={'users': users})


def main_user(request, name):
    return render(request, 'main/main_user.html', context={'user_active': name, 'users': users})
