import json
from typing import List, Type, Any, Dict


def to_dict(obj: Any) -> Dict:
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    elif isinstance(obj, dict):
        return obj
    raise ValueError("Object must have __dict__ attribute or be a dictionary")

def to_json_str(obj: Any) -> str:
    return json.dumps(to_dict(obj), indent=2)

def from_json_str(json_str: str, cls: Type[Any]) -> Any:
    data = json.loads(json_str)
    return cls(**data)

def to_json_file(obj: Any, filename: str) -> None:
    with open(filename, "w") as f:
        json.dump(to_dict(obj), f, indent=2)

def from_json_file(filename: str, cls: Type[Any]) -> Any:
    with open(filename, "r") as f:
        data = json.load(f)
    return cls(**data)

def list_to_json(obj_list: List[Any], filename: str = "data.json") -> None:
    json_list = [to_dict(obj) for obj in obj_list]
    with open(filename, "w") as json_file:
        json.dump(json_list, json_file, indent=2)

def json_to_list(filename: str, cls: Type[Any]) -> List[Any]:
    with open(filename, "r") as json_file:
        data = json.load(json_file)
    return [cls(**entry) for entry in data]

def dicts_to_json(dict_list: List[Dict], filename: str) -> None:
    with open(filename, "w") as f:
        json.dump(dict_list, f, indent=2)

def json_to_dicts(filename: str) -> List[Dict]:
    with open(filename, "r") as f:
        return json.load(f)
    

class Person:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


if __name__ == "__main__":
    p = Person(name="John", age=40)
    json_str = to_json_str(p)
    print("JSON string from object:")
    print(json_str)

    p2 = from_json_str(json_str, Person)
    print("Object from JSON string:")
    print(p2.name, p2.age)

    to_json_file(p, "person.json")

    p3 = from_json_file("person.json", Person)
    print("Object loaded from JSON file:")
    print(p3.name, p3.age)

    persons = [Person(name="Mark", age=23), Person(name="Alice", age=28), Person(name="Bob", age=34)]
    list_to_json(persons, "persons.json")

    loaded_persons = json_to_list("persons.json", Person)
    for person in loaded_persons:
        print(person.name, person.age)

    dict_list = [{"name": "Eve", "age": 29}, {"name": "Frank", "age": 45}]
    dicts_to_json(dict_list, "dicts.json")

    loaded_dicts = json_to_dicts("dicts.json")
    for d in loaded_dicts:
        print(d["name"], d["age"])