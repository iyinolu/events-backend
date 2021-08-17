from django.db import models
from user.models import User

class Events(models.Model):

    TAG_CHOICES = (
        ('Important', 'IMPORTANT'),
        ('Birthday', 'BIRTHDAY'),
        ('Meeting', 'MEETING'),
        ('Leisure', 'LEISURE'),
        ('Hangout', 'HANGOUT')
    )

    date_created = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    content = models.CharField(max_length=500)
    tag = models.CharField(choices=TAG_CHOICES, max_length=50)

