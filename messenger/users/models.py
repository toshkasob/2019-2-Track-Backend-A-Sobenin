from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
    name = models.CharField(max_length=32, verbose_name='имя пользователя')
    nick = models.CharField(max_length=16, verbose_name='ник пользователя')
    avatar = models.TextField(verbose_name='лицо пользователя')