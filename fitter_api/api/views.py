from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Activity, Stats
from api.serializers import ActivitySerializer, StatsSerializer, UserSerializer
from django.http.response import HttpResponse

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    lookup_field= 'username'


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows activities to be viewed or edited
    """
    queryset = Activity.objects.all().order_by('-date')
    serializer_class = ActivitySerializer


class StatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stats to be viewed or edited
    """
    queryset = Stats.objects.all().order_by('-date')
    serializer_class = StatsSerializer
