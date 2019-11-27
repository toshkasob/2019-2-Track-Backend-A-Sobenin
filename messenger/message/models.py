from django.db import models

# Create your models here.
class Message(models.Model):
    chat = models.ForeignKey('chats.Chat', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField()
    added_at = models.DateTimeField()