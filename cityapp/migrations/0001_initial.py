# Generated by Django 4.2.1 on 2023-12-06 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countryapp', '0001_initial'),
        ('stateapp', '0002_rename_country_id_state_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('city_name', models.CharField(db_column='city_name', max_length=120, null=True)),
                ('country', models.ForeignKey(db_column='country_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='countryapp.country')),
                ('state', models.ForeignKey(db_column='state_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='stateapp.state')),
            ],
            options={
                'db_table': 'cities',
            },
        ),
    ]
