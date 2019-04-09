# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 06:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20170630_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='picture_load',
            field=models.ImageField(default='', upload_to='upload'),
        ),
        migrations.AddField(
            model_name='picture',
            name='picture_message',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='picture',
            name='picture_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
