# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0027_auto_20170712_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='School_name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
