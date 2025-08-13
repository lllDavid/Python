class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file  

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print(f"Closing file: {self.filename}")
        if exc_type:
            print(f"An exception occurred: {exc_type}, {exc_value}")
        return False  
    
with FileManager("example.txt", "w") as file:
    file.write("CC\n")
    print("File written successfully.")