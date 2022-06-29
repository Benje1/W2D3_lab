import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jack", 150.00)

    def test_customer_has_name(self):
        self.assertEqual("Jack", self.customer.name)