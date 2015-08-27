# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleves_manager', '0005_auto_20150827_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleve',
            name='annee_elv',
            field=models.ForeignKey(default='AL1', to='eleves_manager.Annee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='annee',
            name='s_annee',
            field=models.ForeignKey(to='eleves_manager.Section'),
        ),
    ]
