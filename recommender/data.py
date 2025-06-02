class Data:
    def __init__(self):
        self.data = {}
        self.category_scores = {}
        self.subcategory_scores = {}  

    def add(self, key: str, value: dict):
        if "score" not in value:
            value["score"] = 0

        if key not in self.data:
            self.data[key] = value
        else:
            self.data[key].update(value)
            if "score" not in self.data[key]:
                self.data[key]["score"] = 0

        category = value.get("category")
        if category not in self.category_scores:
            self.category_scores[category] = 0

        subcat = value.get("subcategory")
        if category and subcat:
            key_subcat = (category, subcat)
            if key_subcat not in self.subcategory_scores:
                self.subcategory_scores[key_subcat] = 0

    def increase_score(self, key, amount=1):
        if key in self.data:
            self.data[key]['score'] += amount
            category = self.data[key].get("category")
            if category:
                self.category_scores[category] += amount
            subcat = self.data[key].get("subcategory")
            if category and subcat:
                self.subcategory_scores[(category, subcat)] += amount
        else:
            print(f"Item {key} not found.")

    def get_product(self, key):
        return self.data.get(key)  

    def get_sorted_by_score(self):
        return sorted(self.data.values(), key=lambda x: x['score'], reverse=True)

    def get_top_categories(self, n=3):
        return sorted(self.category_scores.items(), key=lambda x: x[1], reverse=True)[:n]

    def get_top_subcategories(self, n=3):
        return sorted(self.subcategory_scores.items(), key=lambda x: x[1], reverse=True)[:n]
