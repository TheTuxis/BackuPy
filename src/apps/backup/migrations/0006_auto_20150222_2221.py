# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0005_auto_20150222_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backup',
            name='semanal_day',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Mon', b'Lunes'), (b'Tue', b'Martes'), (b'Web', b'Miercoles'), (b'Thu', b'Jueves'), (b'Fri', b'Viernes'), (b'Sat', b'Sabado'), (b'Sun', b'Domingo')]),
            preserve_default=True,
        ),
    ]
