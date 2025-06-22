import unittest
from unittest.mock import MagicMock

from order_processor import OrderProcessor, InventoryService 


class TestOrderProcessor(unittest.TestCase):
    def setUp(self):
        self.mock_inventory = MagicMock(spec=InventoryService)
        self.processor = OrderProcessor(self.mock_inventory)

    def test_process_order_success(self):
        order = {
            'items': [
                {'id': 'A1', 'quantity': 2, 'price': 10.0},
                {'id': 'B2', 'quantity': 1, 'price': 20.0},
            ],
            'discount': 0.1
        }

        self.mock_inventory.check_stock.side_effect = lambda item_id: 5

        result = self.processor.process_order(order)

        self.assertAlmostEqual(result, 39.6)

    def test_process_order_no_items(self):
        with self.assertRaises(ValueError) as context:
            self.processor.process_order({'items': []})
        self.assertIn("at least one item", str(context.exception))

    def test_process_order_insufficient_stock(self):
        order = {'items': [{'id': 'A1', 'quantity': 3, 'price': 10.0}]}
        self.mock_inventory.check_stock.return_value = 2

        with self.assertRaises(ValueError) as context:
            self.processor.process_order(order)
        self.assertIn("Not enough stock", str(context.exception))

    def test_process_order_invalid_discount(self):
        order = {
            'items': [{'id': 'A1', 'quantity': 1, 'price': 10.0}],
            'discount': 1.5
        }
        self.mock_inventory.check_stock.return_value = 10

        with self.assertRaises(ValueError) as context:
            self.processor.process_order(order)
        self.assertIn("Invalid discount", str(context.exception))

    def test_process_order_no_discount(self):
        order = {'items': [{'id': 'A1', 'quantity': 2, 'price': 15.0}]}
        self.mock_inventory.check_stock.return_value = 10

        result = self.processor.process_order(order)
        expected = 2 * 15 * 1.1 
        self.assertAlmostEqual(result, expected)

    def test_inventory_check_called_for_each_item(self):
        order = {'items': [
            {'id': 'A1', 'quantity': 1, 'price': 10.0},
            {'id': 'B2', 'quantity': 2, 'price': 20.0},
        ]}
        self.mock_inventory.check_stock.return_value = 10

        self.processor.process_order(order)

        calls = [call[0][0] for call in self.mock_inventory.check_stock.call_args_list]
        self.assertListEqual(calls, ['A1', 'B2'])

if __name__ == '__main__':
    unittest.main()