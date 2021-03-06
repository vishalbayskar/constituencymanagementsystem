# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=20)),
                ('population', models.IntegerField(default=0)),
                ('mp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.MP')),
            ],
            options={
                'verbose_name_plural': 'Constituencies',
            },
        ),
    ]
