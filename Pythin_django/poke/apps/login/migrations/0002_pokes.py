# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='got_poked', to='login.User')),
                ('poker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_pokeing', to='login.User')),
            ],
        ),
    ]
