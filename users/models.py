from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TestModel(models.Model):
    name = models.CharField(max_length=20)
    last = models.CharField(max_length=30)
    username = models.CharField(max_length=40)

    def __str__(self):
        return self.username


class DirectMessage(models.Model):
    content = models.CharField(max_length=1000)
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='recipient',  on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True)
    #TODO how can i do this if there is no parent for the first message created? -see stickies, filter reply = none
    # parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:100]

    def blurb(self):
        return self.content[:100]


#TODO extend the Direct message model
class DirectMessageReply(models.Model):
    content = models.CharField(max_length=1000)
    # sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    # recipient = models.ForeignKey(User, related_name='recipient_',  on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True)
    dm_reply = models.ForeignKey(DirectMessage, related_name='dm_reply', on_delete=models.CASCADE)