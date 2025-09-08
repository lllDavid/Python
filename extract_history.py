import sqlite3
import shutil
import os

# Extract unique URLs from Brave browser history and filter by substring

name = os.getlogin()
filter_str = input("Enter a substring to filter URLs by (eg. youtube): ").lower()

history_db_path = fr"C:\Users\{name}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\History"

temp_path = "History_temp"
shutil.copy2(history_db_path, temp_path)

conn = sqlite3.connect(temp_path)
cursor = conn.cursor()

cursor.execute("SELECT DISTINCT url FROM urls")
urls = [url_tuple[0] for url_tuple in cursor.fetchall()]

if filter_str:
    urls = [url for url in urls if filter_str in url.lower()]

output_file = "filtered_urls.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for url in urls:
        f.write(url + "\n")

conn.close()
os.remove(temp_path)

print(f"Extracted {len(urls)} URLs to '{output_file}'")