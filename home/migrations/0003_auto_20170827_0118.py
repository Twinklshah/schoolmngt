# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-26 19:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170827_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultys',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='sections',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='students',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
    ]