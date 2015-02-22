# -*- coding: utf-8 *-*
from django.contrib import admin
from apps.backup.models import Backup, BackupHistory


class AdminBackup(admin.ModelAdmin):
    list_display = (
        'name', 'backup_type', 'periodic', 'active',
        'last_excecute_ok', 'last_excecute_date'
    )
    list_filter = ('backup_type', 'periodic', 'active', 'last_excecute_ok')


class AdminBackupHistory(admin.ModelAdmin):
    list_display = (
        'backup', 'date_created', 'last_excecute_ok'
    )
    list_filter = ('backup', 'date_created', 'last_excecute_ok')

admin.site.register(Backup, AdminBackup)
admin.site.register(BackupHistory, AdminBackupHistory)
