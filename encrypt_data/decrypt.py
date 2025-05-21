from typing import LiteralString

def decrypt_line(line, shift=3) -> LiteralString:
    decrypted_line = []
    for char in line:
        decrypted_char = chr(ord(char) - shift)
        decrypted_line.append(decrypted_char)
    return ''.join(decrypted_line)

input_file = "encrypted_data.txt"
output_file = "decrypted_data.txt"

with open(input_file, "r") as file:
    lines = file.readlines() 

modified_lines = []
for line in lines:
    if line: 
        modified_line = decrypt_line(line) 
        modified_lines.append(modified_line)
    else:
        modified_lines.append(line) 

with open(output_file, "w") as file:
    for line in modified_lines:
        file.write(line) 
        file.write("\n")

print(f"Decrypted data saved as '{output_file}'.")
