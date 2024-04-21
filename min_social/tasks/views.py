from django.shortcuts import render
from rest_framework import permissions, viewsets
from .serializers import *
from rest_framework.permissions import *

class Tasks(object):

    def __init__(self):
        pass

    def get(self, request):
        return render(request, 'tasks.html')
    
    def post(self, request):
        pass


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]