# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleves_manager', '0003_auto_20150827_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annee',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nom_annee', models.CharField(verbose_name='Année', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nom_section', models.CharField(verbose_name='Section', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='annee',
            name='s_annee',
            field=models.ForeignKey(to='eleves_manager.Section'),
        ),
    ]
