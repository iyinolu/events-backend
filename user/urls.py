from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

user_router = DefaultRouter()
user_router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(user_router.urls))
]
