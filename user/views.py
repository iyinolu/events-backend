from tkinter.tix import Tree
from user.models import User
from api.serializers import EventCategorySerializer
from api.models import EventCategory
from rest_framework import viewsets
from rest_framework import permissions, renderers
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.decorators import api_view, action, renderer_classes

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    @action(detail=True, renderer_classes=[renderers.JSONRenderer])
    def categories(self, request, *args, **kwargs):
        # ID:8 is admin user id
        user_categories = EventCategory.objects.filter(owner__in=[self.get_object().id, 8])
        serialized_data = EventCategorySerializer(user_categories, many=True)
        return Response(serialized_data.data)
    