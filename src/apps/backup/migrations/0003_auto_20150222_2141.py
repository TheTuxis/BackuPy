# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backup', '0002_auto_20150222_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='backup',
            name='date_modifier',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='backup',
            name='modifier_by',
            field=models.ForeignKey(related_name='modifier_backup', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
