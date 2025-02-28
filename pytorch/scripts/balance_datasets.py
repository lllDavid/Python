import os
import random

def balance_files(folder_path, keywords, target_count):
    files = os.listdir(folder_path)

    group_files = {keyword: [f for f in files if keyword in f.lower() and os.path.isfile(os.path.join(folder_path, f))]
                   for keyword in keywords}

    counts = {keyword: len(files) for keyword, files in group_files.items()}

    print("Initial counts:")
    for keyword, count in counts.items():
        print(f"{keyword.capitalize()}: {count}")

    if target_count % 2 != 0:
        target_count -= 1

    files_to_delete = []
    for keyword, group in group_files.items():
        if len(group) > target_count:
            excess = len(group) - target_count
            files_to_delete.extend(random.sample(group, excess))

    if not files_to_delete:
        print("The folder is already balanced.")
        return

    for file in files_to_delete:
        os.remove(os.path.join(folder_path, file))
        print(f"Deleted: {file}")

    counts = {keyword: len([f for f in os.listdir(folder_path) if keyword in f.lower() and os.path.isfile(os.path.join(folder_path, f))])
              for keyword in keywords}
    
    print("Final counts:")
    for keyword, count in counts.items():
        print(f"{keyword.capitalize()}: {count}")

folder_path = 'images'
target_count = 1000  
balance_files(folder_path, ['cat', 'dog'], target_count)
