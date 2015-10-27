from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Activity, Stats
from api.serializers import ActivitySerializer, StatsSerializer, UserSerializer, ActivityDetailSerializer
from django.http.response import HttpResponse

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows activities to be viewed or edited
    """
    queryset = Activity.objects.all().order_by('-date')
    serializer_class = ActivitySerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ActivitySerializer
        else:
            return ActivityDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stats to be viewed or edited
    """
    queryset = Stats.objects.all().order_by('-date')
    serializer_class = StatsSerializer

    def get_queryset(self):
        activity_pk = self.kwargs['activity_pk']
        act = get_object_or_404(Activity, pk=activity_pk)
        return self.queryset.filter(activity=act)

    def get_serializer_context(self):
        context = super().get_serializer_context().copy()
        context['activity_pk'] = self.kwargs['activity_pk']
        return context

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
