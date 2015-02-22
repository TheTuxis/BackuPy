from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        from apps.backup.functions import backup_process
        bk_obj = backup_process()
        bk_obj.run_backup()
