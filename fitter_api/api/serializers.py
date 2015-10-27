from rest_framework import serializers
from .models import Activity, Stats
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'id', 'date_joined')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('url', 'id', 'title', 'units', 'date')


class StatsSerializer(serializers.HyperlinkedModelSerializer):
    activity_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True, source="activity")

    class Meta:
        model = Stats
        fields = ('url', 'id', 'activity_id', 'number_of', 'date')

    def create(self, validated_data):
        validated_data['activity_id'] = self.context['activity_pk']
        stat = Stats.objects.create(**validated_data)
        return stat
