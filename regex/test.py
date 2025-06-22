from re import search

paths = [
    r"C:\Users\User\Pictures\Cats\cat.png",
    r"C:\Users\User\Pictures\Cats\cat123.png",
    r"C:\Users\User\Pictures\Cats\cat.123.png",
    r"C:\Users\User\Pictures\Cats\.cat.png",
    r"C:\Users\User\Programs\App\application.exe",
]

pattern = r"\\\.?cat(?:\d+|\.\d+)?\.\w{3,4}$"

for path in paths:
    match = search(pattern, path)
    print(f"{path} -> {match.group(0) if match else 'No match'}")

print(search(r"cat", r"C:\Users\User\Documents\Category\category.txt"))  
print(search(r"cat", r"C:\Users\User\Pictures\Cats\cat.png"))            
print(search(r"cat", r"C:\Users\User\Programs\App\application.exe"))      
