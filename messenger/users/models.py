from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # name = models.CharField(max_length=32, verbose_name='имя пользователя')
    nick = models.CharField(
        max_length=16, 
        verbose_name='ник пользователя', 
        default='', 
        )
    avatar = models.TextField(verbose_name='лицо пользователя')
    
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
