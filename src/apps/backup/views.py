# -*- coding: utf-8 -*-
import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.backup.models import Backup


@login_required
def main(request):
    return render_to_response(
        'main.html',
        RequestContext(
            request,
            {}
        )
    )


@login_required
def list_backup(request):
    backup = Backup.objects.all()
    return render_to_response(
        'backup_list.html',
        RequestContext(
            request,
            {
                'backup': backup
            }
        )
    )


@login_required
def list_files(request, id_backup):
    import time
    file_list = []
    backup = Backup.objects.get(pk=id_backup)
    for filename in os.listdir(backup.destination):
        print filename
        info = os.stat(backup.destination+'/'+filename)
        unidad = 'b.'
        size = info.st_size
        if size > 1024:
            unidad = 'Kb.'
            size = size / 1024
        if size > 1024:
            unidad = 'Mb.'
            size = size / 1024
        if size > 1024:
            unidad = 'Gb.'
            size = size / 1024
        s = {
            'name': filename,
            'size': str(size) + ' '+ unidad,
            'date_create': time.asctime(
                time.localtime(info.st_ctime)
            ),
        }
        file_list.append(s)
    return render_to_response(
        'file_list.html',
        RequestContext(
            request,
            {
                'file_list': file_list,
                'backup': backup
            }
        )
    )


@login_required
def download_backup(request, id_backup, name_file):
    from django.views.static import serve
    backup = Backup.objects.get(pk=id_backup)
    filepath = backup.destination + '/' + name_file
    return serve(
        request, os.path.basename(filepath), os.path.dirname(filepath)
    )
