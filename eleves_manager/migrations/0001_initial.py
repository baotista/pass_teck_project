# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nom_elv', models.CharField(max_length=50)),
                ('pnom_elv', models.CharField(max_length=50)),
                ('dnaiss_elv', models.DateTimeField(verbose_name='date de naissance')),
                ('mail_elv', models.CharField(max_length=100)),
            ],
        ),
    ]
