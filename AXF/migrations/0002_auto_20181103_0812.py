# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-03 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AXF', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtypes',
            name='childtypenames',
            field=models.CharField(max_length=200),
        ),
    ]
