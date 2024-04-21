from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    # image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'