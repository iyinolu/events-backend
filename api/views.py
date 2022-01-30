from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.settings import perform_import
from api.serializers import EventsSerializer, EventCategorySerializer
from api.models import EventCategory, Events
from rest_framework.response import Response
from rest_framework import status



class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [JSONRenderer]
    # TODO: Use filter backends

    def create(self, request, *args, **kwargs):
        """create method that adds request object when perform create is called"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(request, serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        """
        Optionally restrict the retured events for a 
        given user by filtering against `eventdate` parameter in 
        Url.
        """
        # Filter queryset based on a user initiating the request and admin's default categories
        queryset = Events.objects.all().filter(owner=self.request.user.id)
        
        event_date = self.request.query_params.get("eventdate")
        if event_date is not None:
            queryset = queryset.filter(event_date=event_date)
    
        return queryset

    def perform_create(self, request, serializer):
        serializer.save(owner=request.user)

class EventCategoryViewset(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def create(self, request, *args, **kwargs):
        """create method that adds request object when perform create is called"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(request, serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get_queryset(self):    
        # Filter queryset based on a user initiating the request
        queryset = EventCategory.objects.all().filter(owner__in=[self.request.user.id, 8])
        
        return queryset

    def perform_create(self, request, serializer):
        serializer.save(owner=request.user)