# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backup',
            name='last_excecute_date',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='backup',
            name='last_excecute_ok',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
