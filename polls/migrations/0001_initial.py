# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-21 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmsMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.CharField(choices=[('0', 'qq'), ('1', 'aa'), ('2', 'ss'), ('3', 'ee'), ('4', 'mm')], default='1', max_length=4)),
                ('mobile', models.CharField(blank=True, default='', max_length=32, null=True, unique=True)),
                ('message_text', models.CharField(blank=True, default=None, max_length=2046, null=True)),
                ('need_notice', models.BooleanField(default=False)),
            ],
        ),
    ]
