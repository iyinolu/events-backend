from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager):
    """
    Manages the creation of new users
    """

    def create_user(self, username, email, password, **kwargs):
        """Create and return a user with a username, email and password"""
        if username is None:
            raise TypeError("User must have a username.")
        if email is None:
            raise TypeError("User must have an email.")
        if not password:
            raise TypeError("User has not entered a password")

        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """Create User with admin permissions"""
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=50, default="N/A",)
    lastname = models.CharField(max_length=50, default="N/A")
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    # Access the user manager class with the "objects" variable
    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.username


