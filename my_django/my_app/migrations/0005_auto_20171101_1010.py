# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20171101_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(max_length=16),
        ),
    ]
