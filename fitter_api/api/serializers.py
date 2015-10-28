from rest_framework import serializers
from .models import Activity, Stats
from django.contrib.auth.models import User


class StatsSerializer(serializers.HyperlinkedModelSerializer):
    activity_id = serializers.PrimaryKeyRelatedField(many=False,
                                                     read_only=True,
                                                     source="activity")
    # fit_user = serializers.StringRelatedField(read_only=True, source='user')

    class Meta:
        model = Stats
        fields = ('id', 'activity_id', 'number_of', 'date')

    def create(self, validated_data):
        validated_data['activity_id'] = self.context['activity_pk']
        stat = Stats.objects.create(**validated_data)
        return stat


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'password')
        extra_kwargs = {'username': {'write_only': True},
                        'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'title', 'units', 'date')


class ActivityDetailSerializer(ActivitySerializer):
    stats = StatsSerializer(many=True, read_only=True)

    class Meta(ActivitySerializer.Meta):
        fields = tuple(list(ActivitySerializer.Meta.fields) + ['stats'])
