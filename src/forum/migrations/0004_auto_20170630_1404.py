# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 06:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20170630_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='picture_load',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='picture_message',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='picture_time',
        ),
    ]