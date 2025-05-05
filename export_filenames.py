import os

folder_path = os.getcwd()

output_file = os.path.join(folder_path, "file_names_list.txt")

file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

with open(output_file, "w") as f:
    for name in file_names:
        f.write(name + "\n")

print(f"Saved {len(file_names)} filenames to {output_file}")
