# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0068_auto_20170721_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='document',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]