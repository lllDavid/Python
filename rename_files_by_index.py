import os

def rename(path):
    files = os.listdir(path)
    
    for index, value in enumerate(files):
        new_name = f"new words to rename to.{index}{os.path.splitext(value)[1]}"  
        src = os.path.join(path, value)
        dst = os.path.join(path, new_name)
        os.rename(src, dst)

rename("path")