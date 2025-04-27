import os

def find_non_py_files():
    folder_path = os.getcwd()  
    non_py_files = []
    
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if not filename.endswith('.py'):
                non_py_files.append(file_path)
    
    return non_py_files

non_py_files = find_non_py_files()
print("Files that are not .py:")
for file in non_py_files:
    print(file)
