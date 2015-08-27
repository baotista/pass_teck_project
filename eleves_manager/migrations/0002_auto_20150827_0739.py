# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleves_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='dnaiss_elv',
            field=models.DateField(verbose_name='date de naissance'),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='mail_elv',
            field=models.CharField(verbose_name='adresse email', max_length=100),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='nom_elv',
            field=models.CharField(verbose_name="nom de l'élève", max_length=30),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='pnom_elv',
            field=models.CharField(verbose_name="prénom de l'élève", max_length=30),
        ),
    ]
