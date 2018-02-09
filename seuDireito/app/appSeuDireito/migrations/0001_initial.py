# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-08 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advogado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_advogado', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=100)),
                ('ramo_atuacao', models.CharField(max_length=256)),
            ],
        ),
    ]
