# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robo', '0009_auto_20170913_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='robocomprado',
            name='token',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='token'),
        ),
    ]
