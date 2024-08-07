from django.core.management.base import BaseCommand
from pilotlog.exporter import export_to_csv
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Export data to CSV file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'export-logbook_template.csv')
        export_to_csv(file_path)
        self.stdout.write(self.style.SUCCESS('Data exported successfully'))