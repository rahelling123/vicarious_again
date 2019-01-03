from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#TODO figure out if this model is important or not and ditch it
class TestModel(models.Model):
    name = models.CharField(max_length=20)
    last = models.CharField(max_length=30)
    username = models.CharField(max_length=40)

    def __str__(self):
        return self.username


class DirectMessage(models.Model):
    content = models.CharField(max_length=1000)
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='recipient', on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.content[:100]