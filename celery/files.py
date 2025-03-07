from main import process_file
import os

def simulate_file_upload(file_name):
    file_path = os.path.join("uploads", file_name)
    
    result = process_file.delay(file_path)
    
    print(f"Task started for file: {file_name}")
    print("Task result:", result.get())

if __name__ == "__main__":
    simulate_file_upload("data.csv")
