# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleves_manager', '0002_auto_20150827_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='dnaiss_elv',
            field=models.DateField(verbose_name='date de naissance', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='mail_elv',
            field=models.EmailField(max_length=254, verbose_name='adresse mail', blank=True, null=True),
        ),
    ]
