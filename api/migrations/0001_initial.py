# Generated by Django 3.2.6 on 2021-08-17 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('event_date', models.DateTimeField()),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
                ('tag', models.CharField(choices=[('Important', 'IMPORTANT'), ('Birthday', 'BIRTHDAY'), ('Meeting', 'MEETING'), ('Leisure', 'LEISURE'), ('Hangout', 'HANGOUT')], max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
