# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0025_auto_20170710_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=300)),
                ('school_email', models.CharField(max_length=300)),
                ('p_box', models.CharField(max_length=300)),
            ],
        ),
    ]
