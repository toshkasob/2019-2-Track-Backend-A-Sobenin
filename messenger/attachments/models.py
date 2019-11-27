from django.db import models

# Create your models here.
class Attachment(models.Model):
    chat = models.ForeignKey('chats.Chat', on_delete=models.CASCADE)
    message = models.ForeignKey('message.Message', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    type = models.CharField(max_length=16)
    url = models.TextField()
