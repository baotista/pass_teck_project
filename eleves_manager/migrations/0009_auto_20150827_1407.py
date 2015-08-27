# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleves_manager', '0008_auto_20150827_1400'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Annee',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
