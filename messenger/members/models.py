from django.db import models

# Create your models here.
class Member(models.Model):
    user = models.ForeignKey(
        'users.User', 
        on_delete=models.CASCADE, 
        verbose_name='участник чата', 
        )
    chat = models.ForeignKey(
        'chats.Chat', 
        on_delete=models.CASCADE, 
        verbose_name='чат, в котором состоит участник')
    new_messages = models.IntegerField(
        verbose_name='количество непрочитанных сообщений', 
        default=0, 
        )
    last_read_message = models.ForeignKey(
        'message.Message', 
        on_delete=models.PROTECT, 
        verbose_name='последнее прочитанное сообщение', 
        null=True, 
        )

    class Meta:
        verbose_name='участник'
        verbose_name_plural='участники'
