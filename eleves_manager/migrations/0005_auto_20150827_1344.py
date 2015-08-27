# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleves_manager', '0004_auto_20150827_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annee',
            name='s_annee',
            field=models.ForeignKey(to_field='Section', to='eleves_manager.Section'),
        ),
    ]
