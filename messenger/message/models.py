from django.db import models

# Create your models here.
class Message(models.Model):
    chat = models.ForeignKey(
        'chats.Chat', 
        on_delete=models.CASCADE, 
        verbose_name='чат, в котором содержится сообщение', 
        )
    user = models.ForeignKey(
        'users.User', 
        on_delete=models.CASCADE, 
        verbose_name='пользователь, который отправил сообщение', 
        )
    content = models.TextField(
        verbose_name='текст сообщения', 
        default='')
    added_at = models.DateTimeField(
        verbose_name='время отправки сообщения',
        auto_now=True, 
        null=False, 
        )

    class Meta:
        verbose_name='сообщение'
        verbose_name_plural='сообщения'
        ordering=['-added_at']
