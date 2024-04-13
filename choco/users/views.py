from django.shortcuts import render


# Create your views here.

def registration(request):
    return render(request, 'users/registration.html')


def registration_check(request):
    return render(request, 'users/registration_check.html')
