from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from users.models import User

def home_page(request):
    return render(request, 'main/home.html')

def base(request):
    return render(request, 'base.html')

def welcome(request):
    return render(request, 'main/welcome.html')

def main(request):
    users = User.objects.order_by('-id')
    return render(request, 'main/main.html', {'users': users})



