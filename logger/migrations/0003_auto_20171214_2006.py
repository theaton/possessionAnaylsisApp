# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-15 02:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0002_auto_20171214_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='away_team',
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='logger.Team'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='game',
            name='home_team',
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='logger.Team'),
            preserve_default=False,
        ),
    ]
