from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework.settings import perform_import
from api.serializers import EventsSerializer
from api.models import Events



class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer