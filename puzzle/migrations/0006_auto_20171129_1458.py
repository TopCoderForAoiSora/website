# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 14:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('puzzle', '0005_auto_20171129_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerGameHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='puzzle',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]
