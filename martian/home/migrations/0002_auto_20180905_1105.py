# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-05 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dislikes',
            field=models.CharField(blank=True, default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.CharField(blank=True, default='0', max_length=10),
        ),
    ]