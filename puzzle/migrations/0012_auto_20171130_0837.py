# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 08:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0011_auto_20171130_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmanytomany',
            name='solved',
        ),
        migrations.DeleteModel(
            name='TestManyToMany',
        ),
    ]