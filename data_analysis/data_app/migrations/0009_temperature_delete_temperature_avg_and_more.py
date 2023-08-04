# Generated by Django 4.2.3 on 2023-07-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0008_temperature_avg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('month', models.IntegerField(blank=True, null=True)),
                ('month_name', models.CharField(blank=True, max_length=50, null=True)),
                ('day', models.IntegerField(blank=True, null=True)),
                ('year', models.CharField(blank=True, max_length=50, null=True)),
                ('avg_temp_F', models.FloatField(blank=True, null=True)),
                ('avg_temp_C', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Temperature_avg',
        ),
        migrations.DeleteModel(
            name='Temperature_RAW',
        ),
    ]
