# Generated by Django 3.1.1 on 2020-12-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
