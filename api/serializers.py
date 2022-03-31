from rest_framework import serializers 
from api.models import Events, EventCategory


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ["event_date", "title", "content", "tag"]    

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ["pk", "owner", "category_name"]