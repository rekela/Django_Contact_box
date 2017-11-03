# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20171101_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.IntegerField(choices=[(0, 'permanent'), (1, 'of_residence'), (2, 'for_correspondence')], default=0),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='local_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='email_type',
            field=models.IntegerField(choices=[(0, 'private'), (1, 'business')], default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_number',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_type',
            field=models.IntegerField(choices=[(0, 'home'), (1, 'mobile'), (2, 'business')], default=0),
        ),
    ]