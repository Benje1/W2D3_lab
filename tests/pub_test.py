import unittest
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub1 = Pub("Baneermans", 200.00)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(10)
        self.assertEqual(110.00, self.pub.till)

    def test_add_customer_to_pub(self):
        self.pub.add_customer_to_pub("Jack")
        self.assertEqual(1, len(self.pub.customer))


    

    