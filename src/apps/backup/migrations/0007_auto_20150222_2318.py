# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0006_auto_20150222_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backup',
            name='destination',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='backup',
            name='source',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='backuphistory',
            name='last_excecute_ok',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
