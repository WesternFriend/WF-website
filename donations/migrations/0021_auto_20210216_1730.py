# Generated by Django 3.1.1 on 2021-02-16 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0020_auto_20210216_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donatepage',
            old_name='suggested_donation_amounts_once',
            new_name='suggested_donation_amounts',
        ),
    ]
