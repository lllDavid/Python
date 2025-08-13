import pandas as pd

def read_excel(file_path):
    df = pd.read_excel(file_path)
    
    data = df.to_dict(orient='records')
    
    return data

file_path = 'data.xlsx' 
excel_data = read_excel(file_path)

for record in excel_data:
    print(record)