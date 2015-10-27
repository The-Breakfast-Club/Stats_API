from rest_framework import serializers
from .models import Activity, Stats
from django.contrib.auth.models import User


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'title', 'units', 'date')


class StatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stats
        fields = ('url', 'id', 'activity', 'number_of', 'date')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'id', 'date_joined')
    # def create(self, validated_data):
    #     user = User(email=validated_data['email'],
    #                 username=validated_data['username'])
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
