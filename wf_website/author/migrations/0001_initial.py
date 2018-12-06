# Generated by Django 2.1.3 on 2018-12-06 18:44

from django.db import migrations, models
import django_extensions.db.fields
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.CharField(default='', help_text='Enter the given name for a person. This can also be used for an organization name.', max_length=255)),
                ('family_name', models.CharField(blank=True, default='', max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from=['given_name', 'family_name'])),
            ],
            options={
                'db_table': 'author',
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]
