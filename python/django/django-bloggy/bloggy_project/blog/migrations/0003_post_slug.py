# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-17 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171112_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]