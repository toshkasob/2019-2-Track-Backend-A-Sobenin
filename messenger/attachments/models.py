from django.db import models

# Create your models here.
class Attachment(models.Model):
    chat = models.ForeignKey(
        'chats.Chat', 
        on_delete=models.CASCADE, 
        verbose_name='чат, в котором приложенный файл', 
        )
    message = models.ForeignKey(
        'message.Message', 
        on_delete=models.CASCADE, 
        verbose_name='сообщение, к которому приложен файл', 
        )
    user = models.ForeignKey(
        'users.User', 
        on_delete=models.CASCADE, 
        verbose_name='пользователь, который приложил файл', 
        )
    #преименовать с _
    attachment_type = models.CharField(
        max_length=16, 
        verbose_name='тип приложенного файла', 
        default='документ'
        )
    url = models.TextField(verbose_name='ссылка на приложенный файл')

    class Meta:
        verbose_name='приложенный файл'
        verbose_name_plural='приложенные файлы'

