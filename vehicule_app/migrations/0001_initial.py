# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-15 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('position_app', '0009_coordonne_ref'),
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_ref', models.CharField(max_length=200)),
                ('registration', models.CharField(max_length=200)),
                ('container_type', models.CharField(max_length=200)),
                ('container_sub_type', models.CharField(max_length=200)),
                ('volume', models.FloatField()),
                ('height_ex', models.FloatField()),
                ('width_ex', models.FloatField()),
                ('length_ex', models.FloatField()),
                ('height_in', models.FloatField()),
                ('width_in', models.FloatField()),
                ('length_in', models.FloatField()),
                ('weight', models.FloatField()),
                ('capacity', models.FloatField()),
                ('function', models.TextField()),
                ('material', models.CharField(max_length=120)),
                ('container_logo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_registration', models.CharField(max_length=200)),
                ('n_insurance', models.CharField(max_length=200)),
                ('mark', models.CharField(max_length=200)),
                ('v_type', models.CharField(choices=[('CAR', 'Car'), ('TRUCK', 'Truck'), ('VAN', 'Van')], max_length=200)),
                ('v_sub_type', models.CharField(choices=[('CAR1', 'Car1'), ('TRUCK1', 'Truck1'), ('VAN1', 'Van1')], max_length=200)),
                ('v_place_nbr', models.IntegerField(default=0)),
                ('v_average_consumption_city', models.FloatField()),
                ('v_average_consumption_road', models.FloatField()),
                ('physical_state', models.CharField(max_length=200)),
                ('mileage', models.FloatField()),
                ('v_logo', models.FileField(upload_to='')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='position_app.Member')),
            ],
        ),
        migrations.AddField(
            model_name='container',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicule_app.Vehicle'),
        ),
    ]
