import os

def list_files(directory):
    path = os.listdir(directory)
    print("Amount of files: ",len(path))
    
def delete_files_by_amount(directory, amount):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    for i in range(amount):
        file_to_delete = files[i]
        os.remove(os.path.join(directory, file_to_delete))
        print(f"Deleted: {file_to_delete}")
        path = os.listdir(directory)
        print("Amount of files: ",len(path))

list_files(input("Enter path:"))
delete_files_by_amount(input("Enter path:"), int(input("How many to delete?:")))
