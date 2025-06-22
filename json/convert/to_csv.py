import json
import csv

# List of JSON objects/dicts
with open('input.json') as f:
    data = json.load(f)

with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)