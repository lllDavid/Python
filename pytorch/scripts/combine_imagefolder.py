import os
import shutil

# Recursively copies all image files from the source dir and its subdirs into the target dirr

def combine_images(source_folder, target_folder):
    os.makedirs(target_folder, exist_ok=True)

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file_path = os.path.join(root, file)
                shutil.copy(file_path, target_folder)

source_folder = 'satellite_data'
target_folder = 'combined_satellite_images'
combine_images(source_folder, target_folder)
