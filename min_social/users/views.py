from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .forms import LoginForm
from django.contrib import auth
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *

# def registratioin_pole(request):
#     return render(request, 'users/create_user.html')


# def authentification_pole(request):
#     return render(request, 'users/login_form.html')

def profile_pole(request):
    return render(request, 'users/profile.html')

def home_page(request):
    return render(request, 'main/home.html')

def base(request):
    return render(request, 'base.html')

def welcome(request):
    return render(request, 'main/welcome.html')

def main(request):
    users = User.objects.order_by('-id')
    return render(request, 'main/main.html', {'users': users})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username'] #form.cleaned_data['username']
            password = request.POST['password'] #form.cleaned_data['password']
            # cd = form.cleaned_data
            user = auth.authenticate(username=username, password=password)
            if user:
            # if user.is_active:
                login(request, user)
                return render(request, 'users/success.html', {'user': user})
            # else:
                return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'users/login_form.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            new_user.save()
            user = auth.authenticate(username=username, password=password)
            return render(request, 'users/success.html', {'user': user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/create_user.html', {'user_form': user_form})



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]