from django.db import models
from django.conf import settings
from datetime import date

# Create your models here.

class Chat(models.Model):
	created_at = models.DateField(default=date.today)


class Message(models.Model):
	text = models.CharField(max_length=500)
	created_at = models.DateField(default=date.today)
	chat = models.ForeignKey(Chat, on_delete=models.CASCADE,related_name="chat_message_set", default=None, blank=True, null=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="author_message_set") #es geht um Author - Objekt Message als Set
	receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="receiver_message_set")