# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-05 19:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='profile',
            table='profile',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
