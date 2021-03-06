# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-05 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_title', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('number_followers', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='topic_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Topic'),
        ),
    ]
