from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'users', views.UserViewSet)


urlpatterns = [
    path('registration', views.registration, name = 'registration'),
    path('authentification', views.user_login , name = 'authentification'),
    path('', views.index, name = 'index'),
    path('', include(routers.urls)),          #!!!
    path('about', views.about, name = 'about'),
]