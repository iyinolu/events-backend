# Generated by Django 3.2.6 on 2022-01-30 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220130_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventcategory',
            old_name='user',
            new_name='owner',
        ),
    ]