# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='study.Study'),
        ),
    ]
