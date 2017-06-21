# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 10:58
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=128)),
                ('published', models.BooleanField(default=False)),
                ('results_published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('display_name', models.CharField(max_length=128)),
                ('position', models.IntegerField(blank=True, null=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                  related_name='competitors', to='conpo.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=128)),
                ('published', models.BooleanField(db_index=True, default=False)),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='competitions', to='conpo.Event'),
        ),
    ]
