# Generated by Django 3.1.1 on 2020-12-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_donatepage_suggested_donation_amounts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
