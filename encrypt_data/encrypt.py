import os
from typing import LiteralString

def encrypt_line(line, shift=3) -> LiteralString:
    encrypted_line = []
    for char in line:
        encrypted_char = chr(ord(char) + shift)
        encrypted_line.append(encrypted_char)
    return ''.join(encrypted_line)

folder = "data"
files = os.listdir(folder)

for filename in files:
    file_path = os.path.join(folder, filename)
    
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines() 

        modified_lines = []
        for line in lines:
            if line: 
                modified_line = encrypt_line(line)  
                modified_lines.append(modified_line)
            else:
                modified_lines.append(line)

        with open("encrypted_data.txt", "w") as file: 
            file.writelines(modified_lines)

        print(f"File '{filename}' modified and saved as 'encrypted_data.txt'.")
