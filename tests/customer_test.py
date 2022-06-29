import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jack", 150.00, 30)

    def test_customer_has_name(self):
        self.assertEqual("Jack", self.customer.name)
    
    def test_customer_wallet_amount(self):
        self.assertEqual(150.00, self.customer.wallet)

    def test_customer_reduce_wallet(self):
        self.customer.reduce_wallet(10)
        self.assertEqual(140.00, self.customer.wallet)