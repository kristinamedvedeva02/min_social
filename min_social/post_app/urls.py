from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', home_page, name = 'home'),
    path('base', views.base, name = 'base'),
    path('welcome', views.welcome, name = 'welcome'),
    path('main', views.main, name = 'main'),
]