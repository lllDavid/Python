from re import search

path_2 = r"C:\\Users\\User\\Pictures\\Cats\\cat.png"
path_3 = r"C:\\Users\\User\\Pictures\\Cats\\cat123.png"
path_4 = r"C:\\Users\\User\\Pictures\\Cats\\cat.123.png"
path_5 = r"C:\\Users\\User\\Pictures\\Cats\\.cat.png"
path_6 = r"C:\\Users\\User\\Programs\\App\\application.exe"

paths = [path_2, path_3, path_4, path_5, path_6]

pattern = r"(\.?\d*cat(?:\.\d+)?\.\w{3,4})"

for path in paths:
    match = search(pattern, path)
    print(match)
