# Generated by Django 5.0.2 on 2024-02-23 13:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('art_api', '0004_artwork_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Selledartwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('payment', models.CharField(choices=[('Paypal', 'Paypal'), ('Credit Card', 'Credit Card'), ('Klarna', 'Klarna'), ('Bank Transfering', 'Bank Transfering')], max_length=100)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='art_api.artwork')),
            ],
        ),
    ]
