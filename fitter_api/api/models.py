from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Activity(models.Model):
    title = models.CharField(max_length=50)
    units = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='activities')


class Stats(models.Model):
    activity = models.ForeignKey(Activity)
    number_of = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)
