from functools import reduce

cart = [
    {"name": "Laptop", "price": 1000.00, "quantity": 1},
    {"name": "Mouse", "price": 25.00, "quantity": 2},
    {"name": "Headphones", "price": 80.00, "quantity": 1}
]

subtotal = reduce(
    lambda acc, item: acc + (item["price"] * item["quantity"]),
    cart,
    0.0
)

tax_rate = 0.08
total_with_tax = subtotal * (1 + tax_rate)

print(f"Subtotal: ${subtotal:.2f}")
print(f"Total with tax: ${total_with_tax:.2f}")