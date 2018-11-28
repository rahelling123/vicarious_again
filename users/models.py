from django.db import models

# Create your models here.


class TestModel(models.Model):
    name = models.CharField(max_length=20)
    last = models.CharField(max_length=30)
    username = models.CharField(max_length=40)

    def __str__(self):
        return self.username