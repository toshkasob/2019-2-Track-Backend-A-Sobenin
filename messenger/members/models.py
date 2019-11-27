from django.db import models

# Create your models here.
class Member(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    chat = models.ForeignKey('chats.Chat', on_delete=models.CASCADE)
    new_messages = models.IntegerField()
    last_read_message = models.ForeignKey('message.Message', on_delete=models.CASCADE)