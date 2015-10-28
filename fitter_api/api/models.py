from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Activity(models.Model):
    title = models.CharField(max_length=50)
    units = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='activities')


class Stats(models.Model):
    activity = models.ForeignKey(Activity, unique_for_date="date")
    number_of = models.PositiveSmallIntegerField()
    date = models.DateField()

    class Meta:
        unique_together = ('activity', 'date')
