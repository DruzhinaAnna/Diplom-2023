from django.shortcuts import render
from .models import User

def authorization(request):
    return render(request, 'Main/authorization.html')


def registration(request):
    return render(request, 'Main/registration.html')


def register(request):
    return render(request, 'Main/register.html')


def main(request):
    return render(request, 'Main/main.html')