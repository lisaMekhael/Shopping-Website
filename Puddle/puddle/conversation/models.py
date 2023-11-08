import datetime
from time import timezone
from django.db import models
from django.contrib.auth.models import User

from item.models import Item
# Create your models here.

class Conversation (models.Model):
    print("CONVO WAS CALLED")
    item = models.ForeignKey(Item , related_name='conversations' , on_delete=models.CASCADE)
    members = models.ManyToManyField(User , related_name='conversations')
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at' , )



class ConversationMessage (models.Model):
    conversation = models.ForeignKey(Conversation , related_name='messages' ,on_delete=models.CASCADE) #if convo is deleted also messages will be deleted
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User , related_name='created_messages' , on_delete=models.CASCADE)