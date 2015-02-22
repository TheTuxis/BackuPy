# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0003_auto_20150222_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='backup',
            name='incremental_period',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Lunes'), (1, b'Martes'), (2, b'Miercoles'), (3, b'Jueves'), (4, b'Viernes'), (5, b'Sabado'), (6, b'Domingo')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='backup',
            name='mensual_day',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Semanal'), (1, b'Mensual')]),
            preserve_default=True,
        ),
    ]
