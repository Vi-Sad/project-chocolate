from django.shortcuts import render


# Create your views here.


def user_active(user):
    return user


def main(request):
    return render(request, 'main/blocks.html', context={'user_active': user_active('Сладкоежка')})
