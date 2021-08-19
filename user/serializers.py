from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.contrib.auth.hashers import make_password
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'is_active', 'is_staff']

    def validate_password(self, value):
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

