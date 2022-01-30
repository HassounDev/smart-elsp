# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-10 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise_app', '0005_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='MerchandiseDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_type', models.CharField(max_length=250)),
                ('designaiton', models.CharField(max_length=250)),
                ('merchandise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchandise_app.Merchandise')),
            ],
        ),
    ]
