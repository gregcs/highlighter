# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20171013_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='like',
            field=models.IntegerField(blank=True),
        ),
    ]
