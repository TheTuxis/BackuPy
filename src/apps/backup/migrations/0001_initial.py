# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=150, null=True, blank=True)),
                ('source', models.CharField(max_length=20, null=True, blank=True)),
                ('destination', models.CharField(max_length=20, null=True, blank=True)),
                ('backup_type', models.IntegerField(default=0, choices=[(0, b'Incremental'), (1, b'Full')])),
                ('periodic', models.IntegerField(default=0, choices=[(0, b'Diario'), (1, b'Semanal'), (2, b'Mensual')])),
                ('semanal_day', models.IntegerField(blank=True, null=True, choices=[(0, b'Lunes'), (1, b'Martes'), (2, b'Miercoles'), (3, b'Jueves'), (4, b'Viernes'), (5, b'Sabado'), (6, b'Domingo')])),
                ('mensual_day', models.IntegerField(blank=True, null=True, choices=[(0, b'Primer dia'), (1, b'Ultimo dia')])),
                ('active', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
