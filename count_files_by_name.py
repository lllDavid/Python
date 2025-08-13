import os
from collections import Counter

def count_file_types(folder_path, keywords):
    files = os.listdir(folder_path)
    counts = Counter()

    for filename in files:
        if os.path.isfile(os.path.join(folder_path, filename)):
            for keyword in keywords:
                if keyword.lower() in filename.lower():
                    counts[keyword] += 1

    return counts

folder_path = ''
keywords = ['', ''] 

file_counts = count_file_types(folder_path, keywords)

for name, count in file_counts.items():
    print(f"{name}: {count}")