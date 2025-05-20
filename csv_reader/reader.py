import csv

with open('file.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    header = next(csv_reader)
    print("Header:", header)
    
    for row in csv_reader:
        print(row)

def search_in_column(filename, column_name, search_value):
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        matching_rows = [row for row in csv_reader if row[column_name] == search_value]
    return matching_rows

search_in_column("file.csv","first name","Alice")