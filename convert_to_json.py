import json

class Data:
    def __init__(self):
        self.list = [] 
        while True:
            entry = {
                "name": input("Enter name: "),
                "occupation": input("Enter occupation: "),
                "e-mail": input("Enter e-mail: ")
            }
            self.list.append(entry)  
            input_value = input("Continue? Press any key for Yes, type 'No' for No: ")
            if input_value.lower() == "no":
                break

    def save_json(self, filename='data.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.list, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {filename}")

class DataOutput(Data):
    def print_json(self):
        for entry in self.list:
            print(json.dumps(entry))

x = DataOutput()
x.save_json()
x.print_json()