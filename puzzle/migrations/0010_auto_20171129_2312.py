# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0009_testmanytomany'),
    ]

    operations = [
        migrations.AddField(
            model_name='playergamehistory',
            name='toSolve',
            field=models.ManyToManyField(related_name='toSolve', to='puzzle.Puzzle'),
        ),
        migrations.AlterField(
            model_name='playergamehistory',
            name='solved',
            field=models.ManyToManyField(related_name='solved', to='puzzle.Puzzle'),
        ),
    ]
