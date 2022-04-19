# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-26 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facultys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Faculty',
        ),
        migrations.DeleteModel(
            name='section',
        ),
        migrations.RemoveField(
            model_name='students',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='students',
            name='section',
        ),
        migrations.AlterField(
            model_name='students',
            name='mother_name',
            field=models.CharField(max_length=201),
        ),
        migrations.AlterField(
            model_name='students',
            name='roll_no',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]