from django.db import models

# Create your models here.
from django.db.models import ForeignKey
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    author = ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def recent_events(self):
        full_list = Event.objects.all()
        recent_list = full_list[:5]
        return recent_list


class Comment(models.Model):
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
