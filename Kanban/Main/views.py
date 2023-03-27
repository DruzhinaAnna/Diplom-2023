from django.shortcuts import render
from .models import User

def index(request):

    return render(request, 'Main/index.html')


def about(request):
    return render(request, 'Main/about.html')


def register(request):
    return render(request, 'Main/register.html')
