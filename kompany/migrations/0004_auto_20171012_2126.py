# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompany', '0003_auto_20171012_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='slug_name',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
