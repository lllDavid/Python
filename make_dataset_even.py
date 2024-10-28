import os
import random

def balance_files(folder_path, keyword1, keyword2):
    files = os.listdir(folder_path)

    group1_files = [f for f in files if keyword1 in f.lower() and os.path.isfile(os.path.join(folder_path, f))]
    group2_files = [f for f in files if keyword2 in f.lower() and os.path.isfile(os.path.join(folder_path, f))]

    num_group1 = len(group1_files)
    num_group2 = len(group2_files)

    print(f"Initial counts - {keyword1.capitalize()}: {num_group1}, {keyword2.capitalize()}: {num_group2}")

    if num_group1 > num_group2:
        excess = num_group1 - num_group2
        files_to_delete = random.sample(group1_files, excess) 
    elif num_group2 > num_group1:
        excess = num_group2 - num_group1
        files_to_delete = random.sample(group2_files, excess)
    else:
        print("The folder is already balanced.")
        return
    
    for file in files_to_delete:
        os.remove(os.path.join(folder_path, file))
        print(f"Deleted: {file}")

    num_group1 = len([f for f in os.listdir(folder_path) if keyword1 in f.lower() and os.path.isfile(os.path.join(folder_path, f))])
    num_group2 = len([f for f in os.listdir(folder_path) if keyword2 in f.lower() and os.path.isfile(os.path.join(folder_path, f))])
    
    print(f"Final counts - {keyword1.capitalize()}: {num_group1}, {keyword2.capitalize()}: {num_group2}")

folder_path = ''  
balance_files(folder_path, '', '') 
