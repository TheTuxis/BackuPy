# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime

# comentario
BACKUP_TYPE_CHOICES = (
    (0, 'Incremental'),
    (1, 'Full'),
)

BACKUP_PERIODIC_CHOICES = (
    (0, 'Diario'),
    (1, 'Semanal'),
    (2, 'Mensual'),
)

INCREM_PERIODIC_CHOICES = (
    (0, 'Semanal'),
    (1, 'Mensual'),
)

BACKUP_SEMANAL_DAY_CHOICES = (
    ('Mon', 'Lunes'),
    ('Tue', 'Martes'),
    ('Web', 'Miercoles'),
    ('Thu', 'Jueves'),
    ('Fri', 'Viernes'),
    ('Sat', 'Sabado'),
    ('Sun', 'Domingo'),
)

BACKUP_MENSUAL_DAY_CHOICES = (
    (0, 'Primer dia'),
    (1, 'Ultimo dia'),
)


class Backup(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=150, blank=True, null=True)
    source = models.CharField(max_length=300, blank=True, null=True)
    destination = models.CharField(max_length=300, blank=True, null=True)
    backup_type = models.IntegerField(
        choices=BACKUP_TYPE_CHOICES, default=0
    )
    periodic = models.IntegerField(
        choices=BACKUP_PERIODIC_CHOICES, default=0
    )
    semanal_day = models.CharField(
        choices=BACKUP_SEMANAL_DAY_CHOICES, blank=True, null=True, max_length=3
    )
    incremental_period = models.IntegerField(
        choices=INCREM_PERIODIC_CHOICES, blank=True, null=True
    )
    mensual_day = models.IntegerField(
        choices=BACKUP_MENSUAL_DAY_CHOICES, blank=True, null=True
    )
    active = models.BooleanField(default=False)
    last_excecute_ok = models.BooleanField(default=False)
    last_excecute_date = models.DateTimeField(default=datetime.datetime.now)
    modifier_by = models.ForeignKey(
        User, blank=True, null=True, related_name="modifier_backup"
    )
    date_modifier = models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "%s" % (self.name,)


class BackupHistory(models.Model):
    date_created = models.DateTimeField(default=datetime.datetime.now)
    backup = models.ForeignKey(Backup, blank=True, null=True)
    result = models.TextField(max_length=350, blank=True, null=True)
    last_excecute_ok = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s" % (self.backup,)
