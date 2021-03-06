# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-16 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_auto_20180113_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('style', models.CharField(choices=[('Casual', 'Casual'), ('Sport', 'Sport'), ('Business', 'Business'), ('Formal', 'Formal')], max_length=12)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'OTHER')], max_length=12)),
            ],
        ),
    ]
