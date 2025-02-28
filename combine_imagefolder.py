import os
import shutil

def combine_images(source_folder, target_folder):
    os.makedirs(target_folder, exist_ok=True)

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file_path = os.path.join(root, file)
                shutil.copy(file_path, target_folder)

source_folder = 'birds'  
target_folder = 'new_birds'  
combine_images(source_folder, target_folder)
