import os
import argparse
from heapq import nlargest

def collect_sizes(directory, file_list, dir_list):
    try:
        with os.scandir(directory) as entries:
            total_size = 0
            for entry in entries:
                full_path = entry.path
                try:
                    if entry.is_file():
                        size = entry.stat().st_size
                        file_list.append((full_path, size))
                        total_size += size
                    elif entry.is_dir():
                        sub_size = collect_sizes(full_path, file_list, dir_list)
                        total_size += sub_size
                except (PermissionError, OSError):
                    print(f"Skipping: {full_path} (Access Denied)")
                    continue

            dir_list.append((directory, total_size))
            return total_size
    except (PermissionError, OSError):
        print(f"Skipping: {directory} (Access Denied)")
        return 0

def format_size(size):
    if size >= 1024 ** 3:  
        return f"{size / (1024 ** 3):.2f} GB"
    return f"{size / (1024 ** 2):.2f} MB"  

def find_largest_items(directory, num_items=10):
    print(f"Scanning {directory} for largest files and directories (this may take a while)...")
    file_list = []  
    dir_list = []   
    
    collect_sizes(directory, file_list, dir_list)
    
    largest_dirs = nlargest(num_items, dir_list, key=lambda x: x[1])
    print(f"\nTop {min(num_items, len(largest_dirs))} Largest Directories:")
    for dir_path, size in largest_dirs:
        print(f"{dir_path}: {format_size(size)}")
 
    largest_files = nlargest(num_items, file_list, key=lambda x: x[1])
    print(f"\nTop {min(num_items, len(largest_files))} Largest Files:")
    for file_path, size in largest_files:
        print(f"{file_path}: {format_size(size)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find the largest files and directories in a directory and its subdirectories."
    )
    parser.add_argument(
        "directory",
        type=str,
        nargs="?",
        default="C:\\",
        help="Directory to scan (default: C:\\)"
    )
    args = parser.parse_args()
    
    if not os.path.exists(args.directory):
        print("Error: Directory does not exist.")
    else:
        find_largest_items(args.directory)