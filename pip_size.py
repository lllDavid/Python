from os import getlogin, listdir, scandir, path
from collections import defaultdict
from subprocess import run

# NOTE: Matching logic is not 100% accurate
# TODO: Matches wrong on certain packages like "memory-profiler" matches "memory_profiler-0.61.0.dist-info" but should match "memory_profiler.py" so the size is wrong on those

# Retrieve list of installed packages
def get_installed_packages():
    output = run("pip list", capture_output=True, text=True, shell=True).stdout
    packages = output.strip().splitlines()[2:]
    packages = [line.split()[0] for line in packages if line.strip()]
    return packages

# Recursively sum file sizes within a folder
def get_folder_size(folder_path):
    total = 0
    try:
        with scandir(folder_path) as entries:
            for entry in entries:
                if entry.is_file():
                    total += entry.stat().st_size
                elif entry.is_dir():
                    total += get_folder_size(entry.path)
    except PermissionError:
        pass
    return total

# Calculate disk usage for given packages in site-packages directory
def get_package_sizes(packages, user_name):
    dir = fr"C:\Users\{user_name}\AppData\Local\Programs\Python\Python313\Lib\site-packages"
    package_sizes = defaultdict(int)

    dir_entries = listdir(dir)
    normalized_to_original = {entry.lower().replace("-", "_"): entry for entry in dir_entries}

    for package in packages:
        normalized_package = package.lower().replace("-", "_")

        # Try exact folder/file match first using dict lookup
        if normalized_package in normalized_to_original:
            matching_entry = normalized_to_original[normalized_package]
            full_path = path.join(dir, matching_entry)
            if path.isdir(full_path):
                package_sizes[package] = get_folder_size(full_path)
            elif path.isfile(full_path) and full_path.endswith(".py"):
                package_sizes[package] = path.getsize(full_path)
            continue

        # Try folder names starting with package name
        matched = False
        for entry in dir_entries:
            normalized_entry = entry.lower().replace("-", "_")
            if normalized_entry.startswith(normalized_package) and path.isdir(path.join(dir, entry)):
                full_path = path.join(dir, entry)
                package_sizes[package] = get_folder_size(full_path)
                matched = True
                break

        if matched:
            continue

    return package_sizes


def main():
    current_user = getlogin()
    installed_packages = get_installed_packages()
    package_size_map = get_package_sizes(installed_packages, current_user)

    total = 0
    max_package_name_length = max(len(pkg_name) for pkg_name in package_size_map.keys())

    for package_name, size_bytes in package_size_map.items():
        size_mb = size_bytes / (1024 * 1024)
        print(f"Package: {package_name.ljust(max_package_name_length)} Size: {size_mb:8.2f} MB")
        total += size_bytes

    total_size_mb = total / (1024 * 1024)
    total_size_gb = total_size_mb / 1024
    print(f"\nTotal amount of packages: {len(package_size_map)}")
    print(f"Total size of all packages: {total_size_mb:.2f} MB / {total_size_gb:.2f} GB")

if __name__ == "__main__":
    main()