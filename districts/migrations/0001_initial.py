# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 14:59
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlderDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_area', models.IntegerField()),
                ('wards_desc', models.CharField(max_length=50)),
                ('alder', models.CharField(max_length=100)),
                ('lci_ward_g', models.CharField(max_length=50)),
                ('shape_length', models.IntegerField()),
                ('wards', models.IntegerField()),
                ('wards_txt', models.CharField(max_length=2)),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
