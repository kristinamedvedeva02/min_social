from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    base_score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    # image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


# class Score(models.Model):
#     user = models.ForeignKey('users.User', on_delete=models.CASCADE)
#     score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
#     update_date = models.DateTimeField(auto_now_add=True)




# class CreateUserManager(BaseUserManager):
#     def create_user(self, username, password=None):
#         if not username:
#             raise ValueError('Users must have an username')

#         user = self.model(
#             username=username
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None):
#         user = self.create_user(
#             username=username,
#             password=password
#         )
#         user.is_staff = True
#         user.save(using=self._db)
#         return user