from rest_framework import serializers 
from api.models import Events


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ["event_date", "title", "content", "tag"]    
    