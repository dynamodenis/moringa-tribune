# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-19 13:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='titel',
            new_name='title',
        ),
    ]
