# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-19 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=64, verbose_name='State')),
                ('city', models.CharField(max_length=64, verbose_name='City')),
                ('username', models.CharField(max_length=64, verbose_name='User')),
                ('message', models.TextField(verbose_name='Message')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'ordering': ['state', 'city', 'create_time'],
            },
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cities', models.IntegerField(verbose_name='Cities')),
                ('users', models.IntegerField(verbose_name='Users')),
            ],
        ),
    ]
