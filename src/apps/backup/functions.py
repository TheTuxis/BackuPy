import os
from apps.backup.models import Backup, BackupHistory
from datetime import datetime, date

'''
import os
print os.listdir('.')

si queres ejecutar en comando externo:

os.system('comando')



incremental

tar -czvf backup.0.tgz -g backup.snap --exclude="/srv/storage01/lost+found" --exclude=".*" /srv/storage01


tar -czvf backup.1.tgz -g backup.snap --exclude="/srv/storage01/lost+found" --exclude=".*" /srv/storage01
'''


class backup_process:

    def excecute_incremental(self, **kward):
        try:
            destine = kward['destine']
            origin = kward['origin']
            count_backup = 0
            for x in os.listdir(destine):
                if 'backup.' in x and '.tgz' in x:
                    count_backup += 1
            str_command = 'tar -czvf '
            str_command += destine + '/backup.' + str(count_backup) + '.tgz '
            str_command += '-g ' + destine + 'backup.snap '
            str_command += '--exclude="' + destine + '/lost+found" '
            str_command += '--exclude=".*" '
            str_command += origin
            print str_command
            os.system(str_command)
            return {'result': 'OK'}
        except Exception, e:
            return {'result': 'ERROR', 'data': str(e)}

    def clear_incremental(self, **kward):
        try:
            destine = kward['destine']
            str_command = 'rm -R ' + destine + '/*'
            os.system(str_command)
            return {'result': 'OK'}
        except Exception, e:
            return {'result': 'ERROR', 'data': str(e)}

    def excecute_full(self, **kward):
        try:
            destine = kward['destine']
            origin = kward['origin']
            date_str = date.today().strftime('%Y%m%d')
            str_command = 'tar -czvf '
            str_command += destine + '/backup.' + date_str + '.tgz '
            str_command += '--exclude="' + destine + '/lost+found" '
            str_command += '--exclude=".*" '
            str_command += origin
            os.system(str_command)
            return {'result': 'OK'}
        except Exception, e:
            return {'result': 'ERROR', 'data': str(e)}

    def process_backup(self, x):
        today = date.today()
        if x.backup_type == 0:
            if x.incremental_period == 0 and today.strftime("%a") == 'Sun':
                result = self.clear_incremental(destine=x.destination)
                if result['result'] == 'ERROR':
                    return result
            elif today.day == 1:
                result = self.clear_incremental(destine=x.destination)
                if result['result'] == 'ERROR':
                    return result
            result = self.excecute_incremental(
                destine=x.destination, origin=x.source
            )
            if result['result'] == 'ERROR':
                return result
            return result
        else:
            return self.excecute_full(
                destine=x.destination, origin=x.source
            )

    def run_backup(self):
        today = date.today()
        backup_list = Backup.objects.filter(active=True)
        for x in backup_list:
            procesar = False
            if x.periodic == 0:
                procesar = True
            elif x.periodic == 1:
                if x.semanal_day == today.strftime('%a'):
                    procesar = True
            elif x.periodic == 2:
                if x.mensual_day == 0 and today.day == 1:
                    procesar = True
            if procesar:
                result = self.process_backup(x)
                if result['result'] == 'OK':
                    x.last_excecute_ok = True
                    x.last_excecute_date = datetime.now()
                    new_history = BackupHistory(
                        backup=x,
                        result=result['result']
                    )
                    new_history.save()
                else:
                    x.last_excecute_ok = False
                    x.last_excecute_date = datetime.now()
                    new_history = BackupHistory(
                        backup=x,
                        result=result['data'],
                        last_excecute_ok=False
                    )
                    new_history.save()
                x.save()
