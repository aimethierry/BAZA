# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 08:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0073_auto_20170725_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='document',
            new_name='post',
        ),
    ]