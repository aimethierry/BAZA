# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='approved_comment',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.AlterField(
            model_name='answer',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='myblog.Post'),
        ),
    ]
