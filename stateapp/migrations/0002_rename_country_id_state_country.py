# Generated by Django 4.2.1 on 2023-11-23 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stateapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='country_id',
            new_name='country',
        ),
    ]
