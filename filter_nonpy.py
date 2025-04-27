import os

def find_non_py_files():
    folder_path = os.getcwd()  
    non_py_files = []
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and not filename.endswith('.py'):
            non_py_files.append(filename)
    
    return non_py_files

non_py_files = find_non_py_files()
print("Files that are not .py:")
for file in non_py_files:
    print(file)
