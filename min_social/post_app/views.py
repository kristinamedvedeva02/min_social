from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from users.models import User
from rest_framework import viewsets, permissions
from .serializers import *
from django.http import JsonResponse

# def home_page(request):
#     return render(request, 'main/home.html')

# def base(request):
#     return render(request, 'base.html')

# def welcome(request):
#     return render(request, 'main/index.html')

def main(request):
    users = User.objects.order_by('-id')
    return render(request, 'main/main.html', {'users': users})

class OfficeView(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = [permissions.IsAdminUser]

    def init(self):
        pass

    def get(self, request):                 # ??? change
        return JsonResponse({'message': 'This is an office view get'})

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAdminUser]


class OfficeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = [permissions.IsAdminUser]


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAdminUser]







