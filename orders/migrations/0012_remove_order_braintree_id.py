# Generated by Django 3.0.7 on 2020-07-27 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20191204_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='braintree_id',
        ),
    ]
