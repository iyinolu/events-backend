# Generated by Django 3.1.6 on 2021-08-16 13:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20210617_2242'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Events',
        ),
    ]
