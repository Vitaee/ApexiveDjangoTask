# Standard Library
import os

# Django Stuff
from django.conf import settings
from django.core.management.base import BaseCommand

# Applications
from pilotlog.exporter import export_to_csv


class Command(BaseCommand):
    help = "Export data to CSV file"

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, "export-logbook_template.csv")
        export_to_csv(file_path)
        self.stdout.write(self.style.SUCCESS("Data exported successfully"))
