# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0006_auto_20171129_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='playergamehistory',
            name='solved',
            field=models.ManyToManyField(to='puzzle.Puzzle'),
        ),
    ]
