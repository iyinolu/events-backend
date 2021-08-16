from django.shortcuts import render
from rest_framework import permissions
from rest_framework import generics
from rest_framework.settings import perform_import
from api.serializers import EventsSerializer
from api.models import Events


class ListOfTodos(generics.ListAPIView):
    serializer_class = EventsSerializer
    queryset = Events.objects.all()
    permission_classes = [permissions.AllowAny]

class AddTodos(generics.CreateAPIView):
    serializer_class = EventsSerializer
    permission_classes = [permissions.AllowAny]

class DeleteTodo(generics.DestroyAPIView):
    serializer_class = EventsSerializer
