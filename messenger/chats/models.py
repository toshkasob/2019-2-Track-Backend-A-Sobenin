from django.db import models

# Create your models here.
class Chat(models.Model):
    is_group_chat = models.BooleanField(default=False)
    topic = models.CharField(max_length=32)
    last_message = models.TextField()