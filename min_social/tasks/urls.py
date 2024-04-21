from .views import *
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)


urlpatterns = [
    # path('tasks', tasks, name='tasks'),
    # path('add_task', add_task, name='add_task'),
    # path('delete_task', delete_task, name='delete_task'),
    # path('update_task', update_task, name='update_task'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]