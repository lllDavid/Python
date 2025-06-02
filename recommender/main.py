from products import Products
from data import Data
from user import User

def load_products(data, products_dict):
    for cat, subcats in products_dict.items():
        for subcat, prods in subcats.items():
            for p in prods:
                p2 = {**p, "category": cat, "subcategory": subcat}
                data.add(p2["key"], p2)

def simulate_user_views(data, user):
    for k in user.seen:
        data.increase_score(k, 1)

def get_recommendations(data, user):
    seen = set(user.seen)
    items_sorted = data.get_sorted_by_score()
    top_subcats = data.get_top_subcategories()
    top_cats = data.get_top_categories()

    def get_recs(cat=None, subcat=None):
        return [
            i for i in items_sorted
            if (cat is None or i.get("category") == cat) and
               (subcat is None or i.get("subcategory") == subcat) and
               i["key"] not in seen
        ]

    if top_subcats:
        cat, subcat = top_subcats[0][0]
        return get_recs(cat, subcat)

    if top_cats:
        cat = top_cats[0][0]
        return get_recs(cat)

    return []

def main():
    data = Data()
    load_products(data, Products.products)

    user1 = User(
        "product_010", "product_011", "product_007", "product_022",
        "product_018", "product_016", "product_014", "product_046",
        "product_020", "product_049", "product_030", "product_062"
    )
    simulate_user_views(data, user1)

    print("User's Viewed Items Ranked by Score")
    print("\nCategory Scores")
    for c, s in sorted(data.category_scores.items(), key=lambda x: x[1], reverse=True):
        print(f"{c}: {s}")

    print("\nSubcategory Scores")
    for (c, sc), s in sorted(data.subcategory_scores.items(), key=lambda x: x[1], reverse=True):
        print(f"{sc} ({c}): {s}")

    recs = get_recommendations(data, user1)
    print("\nTop Recommendations")
    for r in recs:
        print(f" - {r['name']} ({r['category']} > {r['subcategory']}) | Score: {r['score']}")

if __name__ == "__main__":
    main()
