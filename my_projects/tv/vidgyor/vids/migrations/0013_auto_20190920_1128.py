# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-20 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vids', '0012_auto_20190920_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='categories',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
