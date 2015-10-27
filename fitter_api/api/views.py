from django.shortcuts import render
from rest_framework import viewsets
from .models import Activity
from api.serializers import ActivitySerializer
from django.http.response import HttpResponse

# Create your views here.

class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows activities to be viewed or edited
    """
    queryset = Activity.objects.all().order_by('-date')
    serializer_class = ActivitySerializer
