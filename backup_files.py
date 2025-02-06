import os
import shutil
import time

def backup_files(src_dir, dest_dir):
    try:
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        backup_dir = os.path.join(dest_dir, f"backup_{timestamp}")
        os.makedirs(backup_dir)
        
        for file_name in os.listdir(src_dir):
            full_file_name = os.path.join(src_dir, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, os.path.join(backup_dir, file_name))
        
        print(f"Backup successful. Files backed up to {backup_dir}")
    
    except Exception as e:
        print(f"Error during backup: {e}")

backup_files('/path/to/source/folder', '/path/to/backup/folder')
