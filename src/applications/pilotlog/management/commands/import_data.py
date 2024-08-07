from django.core.management.base import BaseCommand
from pilotlog.importer import import_data
from django.conf import settings
import os


class Command(BaseCommand):
    help = 'Import data from JSON file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'pilotlog_mcc.json')
        import_data(file_path)
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
