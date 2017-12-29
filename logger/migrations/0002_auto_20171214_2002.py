# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-15 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ('date',)},
        ),
        migrations.RemoveField(
            model_name='game',
            name='team',
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ManyToManyField(related_name='away_team', to='logger.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ManyToManyField(related_name='home_team', to='logger.Team'),
        ),
    ]