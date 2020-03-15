from django.db import models

# Create your models here.
class Chat(models.Model):
    is_group_chat = models.BooleanField(
        default=False, 
        verbose_name='признак группового чата', 
        )
    topic = models.CharField(
        max_length=255, 
        verbose_name='тема/название чата', 
        )
    last_message = models.TextField(
        verbose_name='последнее сообщение', 
        null=True, 
        default=None, 
        )
        
    def __str__(self):
        return self.topic

    class Meta:
        verbose_name='чат'
        verbose_name_plural='чаты'
