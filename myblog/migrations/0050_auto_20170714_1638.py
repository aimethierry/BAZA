# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 14:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0049_auto_20170714_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='password',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='profile_pc',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='school',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='text',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user_firstname',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user_lastname',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user_name',
        ),
        migrations.AddField(
            model_name='teacher',
            name='School',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='myblog.Post'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
