from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework.settings import perform_import
from api.serializers import EventsSerializer
from api.models import Events



class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """create method that adds request object when perform create is called"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(request, serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, request, serializer):
        serializer.save(owner=request.user)