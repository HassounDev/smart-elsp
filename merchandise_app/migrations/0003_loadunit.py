# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-09 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise_app', '0002_auto_20170309_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoadUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=400)),
                ('number_of_products', models.IntegerField()),
                ('volume', models.FloatField()),
                ('width_lu', models.FloatField()),
                ('length_lu', models.FloatField()),
                ('height_lu', models.FloatField()),
                ('value_lu', models.FloatField()),
                ('state_lu', models.CharField(max_length=250)),
                ('physical_state', models.CharField(max_length=250)),
                ('merchandise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchandise_app.Merchandise')),
            ],
        ),
    ]
