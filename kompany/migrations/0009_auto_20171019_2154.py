# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompany', '0008_auto_20171019_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptops',
            name='slug_name',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
