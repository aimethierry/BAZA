# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0061_document_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myblog.Document'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]
