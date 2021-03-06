# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 03:57
from __future__ import unicode_literals

from django.db import migrations
import django_rdkit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial_application', '0002_create_compound_molecule_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='compound',
            name='ffp2',
            field=django_rdkit.models.fields.BfpField(null=True),
        ),
        migrations.AddField(
            model_name='compound',
            name='mfp2',
            field=django_rdkit.models.fields.BfpField(null=True),
        ),
        migrations.AddField(
            model_name='compound',
            name='torsionbv',
            field=django_rdkit.models.fields.BfpField(null=True),
        ),
    ]
