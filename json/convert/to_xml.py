import json
from dicttoxml import dicttoxml

# List of JSON objects/dicts
with open('input.json') as f:
    data = json.load(f)

xml = dicttoxml(data, custom_root='people', attr_type=False)

with open('output.xml', 'wb') as f:
    f.write(xml)