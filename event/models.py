from django.db import models


# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    def recent_events(self):
        full_list = Event.objects.all()
        recent_list = full_list[:5]
        return recent_list