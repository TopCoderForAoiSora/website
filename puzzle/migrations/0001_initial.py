# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.IntegerField()),
                ('point', models.IntegerField()),
                ('content', models.CharField(max_length=1000)),
                ('logo', models.CharField(max_length=250)),
            ],
        ),
    ]