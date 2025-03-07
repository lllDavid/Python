import pandas as pd
from celery import Celery

app = Celery('file_processing', broker='redis://localhost:6379/0')

@app.task
def process_file(file_path):
    print(f"Processing file: {file_path}")
    
    try:
        data = pd.read_csv(file_path)
        
        if data.isnull().any().any():
            raise ValueError("File contains invalid data (missing values).")
        
        print(f"File {file_path} processed successfully with {len(data)} records.")
        
        for index, row in data.iterrows():
            print(f"Saving record: {row.to_dict()}")
        
        return f"File {file_path} processed successfully."
    
    except Exception as e:
        return f"Error processing file {file_path}: {str(e)}"
