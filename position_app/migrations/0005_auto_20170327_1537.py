# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-27 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position_app', '0004_auto_20170313_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='ref',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='link',
            name='type_road',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='member',
            name='adress',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='member',
            name='fax',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='member',
            name='m_type',
            field=models.CharField(choices=[('LOADER', 'Loader'), ('WAREHOUSEMAN', 'Warehouseman'), ('TRANSPORTER', 'Transporter')], max_length=250),
        ),
        migrations.AlterField(
            model_name='member',
            name='tele',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='point',
            name='function',
            field=models.CharField(choices=[('GARAGE', 'Garage'), ('RESRT AREA', 'Rest Area'), ('PAYING', 'Paying'), ('PARK', 'Park'), ('CUSTOMS', 'Customs'), ('OTHERS', 'Others')], max_length=250),
        ),
        migrations.AlterField(
            model_name='point',
            name='ref',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='position',
            name='function',
            field=models.CharField(choices=[('GARAGE', 'Garage'), ('RESRT AREA', 'Rest Area'), ('PAYING', 'Paying'), ('PARK', 'Park'), ('CUSTOMS', 'Customs'), ('OTHERS', 'Others')], max_length=250),
        ),
        migrations.AlterField(
            model_name='position',
            name='ref',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='service',
            name='label',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='service',
            name='s_type',
            field=models.CharField(choices=[('LOADING', 'Loading'), ('UNLOADING', 'Unloading')], max_length=250),
        ),
        migrations.AlterField(
            model_name='service',
            name='value',
            field=models.CharField(max_length=250),
        ),
    ]