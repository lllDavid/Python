import os
import pandas as pd

PATH = " "

files = os.listdir(f'{PATH}')
raw_data = {'fname': [], 'label': []}
for fname in files:
  raw_data['fname'].append(fname)
  raw_data['label'].append(fname[:3])

df = pd.DataFrame(raw_data, columns = ['fname', 'label'])
df.to_csv(f'{PATH}labels.csv', index = False)
df.head()