def write_to_file():
    with open('example.txt', 'w') as file:
        file.write("Hello, this is a test file.\n")
        file.write("Let's add some more text to it.\n")
    print("File written successfully.")

def read_from_file():
    try:
        with open('example.txt', 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("The file does not exist!")

def append_to_file():
    with open('example.txt', 'a') as file:
        file.write("This is an appended line.\n")
    print("Content appended successfully.")

def read_lines_from_file():
    try:
        with open('example.txt', 'r') as file:
            lines = file.readlines()
            print("File lines:")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("The file does not exist!")

def main():
    write_to_file()
    read_from_file()
    append_to_file()
    read_lines_from_file()

if __name__ == "__main__":
    main()