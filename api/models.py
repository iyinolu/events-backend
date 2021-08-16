from django.db import models
from django.contrib.auth.models import User

class Events(models.Model):
    COLOR_CHOICES = (
        ('Red', 'RED'),
        ('Green', 'GREEN'),
        ('Blue', 'BLUE')
    )

    STATUS_CHOICES = (
        ('Active', 'ACTIVE'),
        ('Completed', 'COMPLETED'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    content = models.CharField(max_length=500)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    color = models.CharField(choices=COLOR_CHOICES, max_length=8)

