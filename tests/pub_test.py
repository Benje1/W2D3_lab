import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestPub(unittest.TestCase):
    
    
    def setUp(self):
        self.customer =  Customer("Jack", 150.00, 30)
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub1 = Pub("Baneermans", 200.00)
        self.drink = Drink("Beer", 10, 1)
        self.food = Food("Burgher", 30, 2)

        # {name: ....
        # alcohol: ...
        # number_of: ...}
        #Change all drinks append,
        #function reduces number of
        # name a list of and pass it on?
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(10)
        self.assertEqual(110.00, self.pub.till)

    def test_add_customer_to_pub(self):
        self.pub.add_customer_to_pub(self.customer)
        self.assertEqual(1, len(self.pub.customers))

    def test_sell_drink_to_customer(self):
        self.pub.add_drink(self.drink)
        self.pub.add_customer_to_pub(self.customer)
        self.pub.sell_drink_to_customer(self.customer, self.drink)
        self.assertEqual(110.00, self.pub.till)
        self.assertEqual(140.00, self.customer.wallet)
        self.assertEqual(1, len(self.customer.drinks))
    
    def test_check_customer_age(self):
        customer1 = Customer("Sam", 40.00, 17)
        self.pub.add_customer_to_pub(customer1)
        self.pub.sell_drink_to_customer(customer1, self.drink)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(40.00, customer1.wallet)
    
    def test_check_drunkeness_of_customer(self):
        self.pub.add_drink(self.drink)
        self.pub.add_drink(self.drink)
        counter = 0
        self.pub.add_customer_to_pub(self.customer)
        while counter < 6:
            self.pub.sell_drink_to_customer(self.customer, self.drink)
            counter += 1
        self.assertEqual(5, self.customer.alcohol_level)
    
    def test_customer_has_eaten(self):
        self.pub.add_customer_to_pub(self.customer)
        self.pub.sell_food_to_customer(self.customer, self.food)
        self.assertEqual(-2, self.customer.alcohol_level)
    
    def test_check_food_and_drink(self):
        self.pub.add_drink(self.drink)
        self.pub.add_drink(self.drink)
        self.pub.add_drink(self.drink)
        counter = 0
        self.pub.add_customer_to_pub(self.customer)
        self.pub.sell_food_to_customer(self.customer, self.food)
        while counter < 6:
            self.pub.sell_drink_to_customer(self.customer, self.drink)
            counter += 1
        self.assertEqual(4, self.customer.alcohol_level)
        self.assertEqual(6, len(self.customer.drinks))
    
    def test_check_stock(self):
        self.pub.add_drink(self.drink)
        self.assertEqual(3, self.pub.check_stock_level(self.drink))
    