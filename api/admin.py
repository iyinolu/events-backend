from django.contrib import admin
from api.models import Events, EventCategory

# Register models
admin.site.register(Events)
admin.site.register(EventCategory)