import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    
    def setUp(self):
        self.customer =  Customer("Jack", 150.00, 30)
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub1 = Pub("Baneermans", 200.00)
        self.drink = Drink("Beer", 10)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(10)
        self.assertEqual(110.00, self.pub.till)

    def test_add_customer_to_pub(self):
        self.pub.add_customer_to_pub("Jack")
        self.assertEqual(1, len(self.pub.customer))

    def test_sell_drink_to_customer(self):
        self.pub.add_customer_to_pub(self.customer)
        self.pub.sell_drink_to_customer(self.customer, self.drink.price)
        self.assertEqual(110.00, self.pub.till)
        self.assertEqual(140.00, self.customer.wallet)
    

    