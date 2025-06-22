class InventoryService:
    def check_stock(self, item_id):
        # Mock calls an external system
        raise NotImplementedError()

class OrderProcessor:
    TAX_RATE = 0.1

    def __init__(self, inventory_service):
        self.inventory_service = inventory_service

    def process_order(self, order):
        """
        order = {
            'items': [{'id': 'A1', 'quantity': 2, 'price': 10.0}, ...],
            'discount': 0.1  # 10% discount optional
        }
        """
        if 'items' not in order or not order['items']:
            raise ValueError("Order must have at least one item")

        total = 0
        for item in order['items']:
            if self.inventory_service.check_stock(item['id']) < item['quantity']:
                raise ValueError(f"Not enough stock for item {item['id']}")
            total += item['quantity'] * item['price']

        if 'discount' in order:
            if not (0 <= order['discount'] < 1):
                raise ValueError("Invalid discount")
            total *= (1 - order['discount'])

        total_with_tax = total * (1 + self.TAX_RATE)
        return round(total_with_tax, 2)