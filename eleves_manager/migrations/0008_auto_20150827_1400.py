# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleves_manager', '0007_auto_20150827_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annee',
            name='s_annee',
        ),
        migrations.RemoveField(
            model_name='eleve',
            name='annee_elv',
        ),
    ]
