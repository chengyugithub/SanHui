# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0007_auto_20171213_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnelinformation',
            name='group',
            field=models.CharField(choices=[('1', '一组'), ('2', '二组'), ('3', '三组'), ('4', '四组'), ('5', '五组'), ('6', '六组'), ('7', '七组')], max_length=4, verbose_name='组数'),
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='is_basic_living_allowances',
            field=models.CharField(choices=[('db', '低保'), ('w', '无')], default='w', max_length=3, verbose_name='最低保障'),
        ),
    ]
