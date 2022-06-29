class Pub:
    def __init__(self, _pub_name, _till):
        self.name = _pub_name
        self.till = _till
        self.customers = []
        # self.drink = []
    
    def increase_till(self, amount):
        self.till += amount

    def add_customer_to_pub(self, customer):
        self.customers.append(customer)

    
    def sell_drink_to_customer(self, customer, drink):
        if customer.age >= 18 and customer.alcohol_level < 5:
            customer.buy_drink(drink)
            self.increase_till(drink.price)
