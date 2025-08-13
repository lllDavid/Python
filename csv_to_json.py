import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    csv_to_json('data.csv', 'data.json')