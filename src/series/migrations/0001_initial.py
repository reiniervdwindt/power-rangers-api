# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-05 12:58
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('number', models.PositiveSmallIntegerField()),
                ('year', models.PositiveSmallIntegerField()),
                ('parent',
                 models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                   to='series.Series')),
            ],
            options={
                'ordering': ('year',),
                'verbose_name_plural': 'series',
            },
        ),
    ]
