# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight_server', '0002_auto_20161120_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='user_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
