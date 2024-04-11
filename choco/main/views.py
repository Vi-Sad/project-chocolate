from django.shortcuts import render

# Create your views here.

user_active = 'Гость'


def main(request):
    return render(request, 'main/blocks.html', context={'user_active': user_active})
