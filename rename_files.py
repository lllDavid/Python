import os

directory = ''

files = os.listdir(directory)
image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

for i, filename in enumerate(image_files):
    new_name = f'.{i}.jpg'
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

print("Renaming completed.")
