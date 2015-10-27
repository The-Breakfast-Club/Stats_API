from rest_framework import serializers
from .models import Activity, Stats
from django.contrib.auth.models import User


class ActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Activity
        fields = ('id', 'title', 'units', 'date', 'user')


class StatsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stats
        fields = ('id', 'activity', 'number_of', 'date')

        
