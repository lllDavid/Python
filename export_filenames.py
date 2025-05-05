# This script recursively finds all .py files in the current directory and its subdirectories, and writes their relative paths to a txt file

import os

folder_path = os.getcwd()

output_file = os.path.join(folder_path, "py_files.txt")

py_files = []

for dirpath, dirnames, filenames in os.walk(folder_path):
    for file in filenames:
        if file.endswith(".py"):
            full_path = os.path.join(dirpath, file)
            relative_path = os.path.relpath(full_path, folder_path)
            py_files.append(relative_path)

with open(output_file, "w") as f:
    for file_path in py_files:
        f.write(file_path + "\n")

print(f"Saved {len(py_files)} .py files to {output_file}")
