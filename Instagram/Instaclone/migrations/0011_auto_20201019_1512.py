# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-19 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instaclone', '0010_auto_20201019_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
