from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'users', views.UserViewSet)


urlpatterns = [
    path('registration', views.registration, name = 'registration'),
    path('authentification', views.user_login , name = 'authentification'),
    path('profile', profile_pole, name = 'profile'),
    path('', include(routers.urls)),
]