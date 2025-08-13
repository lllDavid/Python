import csv

def parse_csv(file_path):
    data = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

file_path = 'data.csv' 
parsed_data = parse_csv(file_path)

for record in parsed_data:
    print(record)