import ijson
from .models import Aircraft

def import_data(file_path):
    with open(file_path, 'r') as file:
        objects = ijson.items(file, 'item')
        for entry in objects:
            Aircraft.objects.update_or_create(
                guid=entry['guid'],
                defaults={
                    'user_id': entry['user_id'],
                    'make': entry['meta']['Make'],
                    'model': entry['meta']['Model'],
                    'reference': entry['meta']['Reference'],
                    'modified': entry['_modified']
                }
            )
