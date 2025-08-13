import os
import pandas as pd

def search_csv_files(directory):
    csv_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                csv_files.append(os.path.join(root, file))
    return csv_files

def main():
    search_directory = input("Enter the directory path to search for CSV files: ")

    csv_files = search_csv_files(search_directory)

    if not csv_files:
        print("No CSV files found in the specified directory.")
    else:
        print("Found CSV files:")
        for i, csv_file in enumerate(csv_files):
            print(f"{i + 1}: {csv_file}")

        file_choice = input("Enter the number of the file you want to open (or 'q' to quit): ")
        if file_choice.isdigit() and 1 <= int(file_choice) <= len(csv_files):
            chosen_file = csv_files[int(file_choice) - 1]
            try:
                data = pd.read_csv(chosen_file)
                print("CSV file opened successfully:")
                print(data.head()) 
            except Exception as e:
                print(f"Error opening the file: {e}")
        elif file_choice.lower() == 'q':
            print("Exiting without opening a file.")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()