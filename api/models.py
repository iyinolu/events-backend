from django.db import models
from user.models import User

class EventCategory(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=10, blank=False)    

class Events(models.Model):    
    date_created = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, blank=False)
    content = models.CharField(max_length=500)
    tag = models.ForeignKey(EventCategory, on_delete=models.CASCADE, null=True)    
    

