# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20180524_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='result',
            field=models.CharField(default='pending', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='result',
            field=models.CharField(default='pending', max_length=10),
            preserve_default=False,
        ),
    ]