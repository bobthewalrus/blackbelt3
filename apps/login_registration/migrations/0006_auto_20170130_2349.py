# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 23:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0005_auto_20170130_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pokecount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(default=datetime.datetime(2017, 1, 30, 23, 49, 35, 218130)),
        ),
    ]
