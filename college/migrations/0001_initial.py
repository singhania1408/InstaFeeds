# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-09 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=100)),
                ('icon', models.ImageField(max_length=200, upload_to=b'')),
                ('coverImage', models.ImageField(max_length=200, upload_to=b'')),
            ],
        ),
    ]