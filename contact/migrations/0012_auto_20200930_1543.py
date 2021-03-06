# Generated by Django 3.1.1 on 2020-09-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0011_auto_20200930_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingaddress',
            name='country',
            field=models.CharField(default='United States', max_length=255),
        ),
        migrations.AlterField(
            model_name='meetingaddress',
            name='locality',
            field=models.CharField(help_text='Locality or city.', max_length=255),
        ),
    ]
