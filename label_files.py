import os
import pandas as pd

PATH = "images"

files = os.listdir(PATH)
raw_data = {'filename': [], 'label': []}

for filename in files:
    raw_data['filename'].append(filename)

    period_index = filename.find('.')
    
    if period_index != -1:
        label = filename[:period_index] 
    else:
        label = filename  

    raw_data['label'].append(label)

df = pd.DataFrame(raw_data, columns=['filename', 'label'])
df.to_csv(f'{PATH}/labels.csv', index=False)
print(df.head())