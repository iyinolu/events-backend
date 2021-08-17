from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'events', views.EventsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
