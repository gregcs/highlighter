# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20171101_1420'),
        ('study', '0004_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='user_set',
            field=models.ManyToManyField(blank=True, to='accounts.Profile'),
        ),
    ]