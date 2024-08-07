import pandas as pd
from .models import Aircraft

def export_to_csv(file_path):
    aircrafts = Aircraft.objects.all().values('id', 'make', 'model', 'reference', 'modified')
    
    df = pd.DataFrame.from_records(aircrafts)
    
    df.rename(columns={
        'id': 'AircraftID',
        'make': 'Make',
        'model': 'Model',
        'reference': 'Reference',
        'modified': 'Modified'
    }, inplace=True)
    
    df.to_csv(file_path, index=False)