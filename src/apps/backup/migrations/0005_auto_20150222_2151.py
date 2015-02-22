# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0004_auto_20150222_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackupHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('result', models.TextField(max_length=350, null=True, blank=True)),
                ('last_excecute_ok', models.BooleanField(default=False)),
                ('backup', models.ForeignKey(blank=True, to='backup.Backup', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='backup',
            name='incremental_period',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Semanal'), (1, b'Mensual')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='backup',
            name='mensual_day',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Primer dia'), (1, b'Ultimo dia')]),
            preserve_default=True,
        ),
    ]
