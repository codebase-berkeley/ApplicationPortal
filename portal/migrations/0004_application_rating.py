# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20171029_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
