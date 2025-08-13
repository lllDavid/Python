def run_dynamic_model():
    class_code = """
class DynamicModel:
    def __init__(self, name):
        self.name = name
        self.fields = {}

    def add_field(self, key, value):
        self.fields[key] = value

    def describe(self):
        print(f"Model: {self.name}")
        for k, v in self.fields.items():
            print(f"  {k}: {v}")
"""

    local_namespace = {}

    exec(class_code, globals(), local_namespace)

    usage_code = """
model = DynamicModel("Product")
model.add_field("name", "Laptop")
model.add_field("price", "$1200")
model.add_field("stock", 42)
model.describe()
"""

    exec(usage_code, globals(), local_namespace)

run_dynamic_model()