# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 00:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0006_auto_20170130_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(default=datetime.datetime(2017, 1, 31, 0, 20, 3, 397227)),
        ),
    ]