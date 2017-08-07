# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0036_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='picture',
        ),
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='profile_pc',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]
