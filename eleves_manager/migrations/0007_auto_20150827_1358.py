# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleves_manager', '0006_auto_20150827_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annee',
            name='s_annee',
        ),
        migrations.AddField(
            model_name='annee',
            name='s_annee',
            field=models.ManyToManyField(to='eleves_manager.Section'),
        ),
    ]
