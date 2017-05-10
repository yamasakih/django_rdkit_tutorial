# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 01:11
from __future__ import unicode_literals

from django.db import migrations, models
import django_rdkit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('molecule', django_rdkit.models.fields.MolField()),
            ],
        ),
    ]
