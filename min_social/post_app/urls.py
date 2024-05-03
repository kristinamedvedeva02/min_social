from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers

routers = routers.SimpleRouter()
routers.register(r'api/companies', views.CompanyViewSet)
routers.register(r'api/offices', views.OfficeViewSet)
routers.register(r'api/teams', views.TeamViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    # path('offices/', views.OfficeListView.as_view(), name = 'offices', ),  #??? change
    # path('offices/<int:pk>/', OfficeDetail.as_view()),
    # path('teams', views.teams, name = 'teams'),
    # path('companies', views.companies, name = 'companies'),
]