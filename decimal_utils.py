from decimal import Decimal
import json

# Convert Decimal to string 
def decimal_serializer(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError(f"Type {type(obj)} not serializable")

# Parse JSON string to Python object
def deserialize_data(data):
    if isinstance(data, str):
        return json.loads(data)
    return data

# Convert dictionary to Decimal
def convert_to_decimal(data):
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary")
    return {key: Decimal(value) if isinstance(value, str) else value for key, value in data.items()}



data = {'price': Decimal('19.99'), 'tax': Decimal('1.50')}

json_str = json.dumps(data, default=decimal_serializer)
print("Serialized JSON:", json_str)

obj = deserialize_data(json_str)
print("Deserialized object:", obj)

obj_decimal = convert_to_decimal(obj)
print("Converted to Decimal:", obj_decimal)