import json

class JsonTool:
    def __init__(self):
        pass
    
    def load_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
        except json.JSONDecodeError:
            print(f"Error: The file '{file_path}' contains invalid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def save_json(self, data, file_path, indent=4):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=indent)
            print(f"Data has been written to {file_path}")
        except Exception as e:
            print(f"Error saving JSON to {file_path}: {e}")
    
    def pretty_print_json(self, data):
        try:
            print(json.dumps(data, indent=4))
        except Exception as e:
            print(f"Error while pretty printing JSON: {e}")
    
    def validate_json(self, json_string):
        try:
            json.loads(json_string)
            print("The provided string is valid JSON.")
        except json.JSONDecodeError:
            print("The provided string is not valid JSON.")

if __name__ == "__main__":
    json_tool = JsonTool()

    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    json_tool.save_json(data, 'data.json')

    loaded_data = json_tool.load_json('data.json')

    if loaded_data:
        json_tool.pretty_print_json(loaded_data)

    json_string = '{"name": "Alice", "age": 25}'
    json_tool.validate_json(json_string)
    
    invalid_json_string = '{"name": "Bob", "age": 30,}'
    json_tool.validate_json(invalid_json_string)
