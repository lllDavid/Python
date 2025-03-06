from re import search

path = r"C:\\Users\\User\\Documents\\Category\\category.txt"

path_2 = r"C:\\Users\\User\\Pictures\\Cats\\cat.png"

path_3 = r"C:\\Users\\User\\Programs\\App\\application.exe"

print(search(r"cat", path))  

print(search(r"cat", path_2))  

print(search(r"cat", path_3))  