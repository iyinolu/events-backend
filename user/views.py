from user.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from django.contrib.auth import get_user_model
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


    