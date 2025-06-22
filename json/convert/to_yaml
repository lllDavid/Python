import json
import yaml

# List of JSON objects/dicts
with open('input.json') as f:
    data = json.load(f)

with open('output.yaml', 'w') as yamlfile:
    yaml.safe_dump(data, yamlfile, default_flow_style=False)