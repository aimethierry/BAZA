# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0019_remove_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myblog.Comment'),
        ),
    ]
