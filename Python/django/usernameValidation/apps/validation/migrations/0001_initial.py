# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-21 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usernames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
