# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-21 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filtertest.Manufacturer')),
            ],
        ),
    ]
