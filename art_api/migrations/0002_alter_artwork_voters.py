# Generated by Django 5.0.2 on 2024-02-21 13:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='voters',
            field=models.ManyToManyField(blank=True, null=True, related_name='voted_images', to=settings.AUTH_USER_MODEL),
        ),
    ]
