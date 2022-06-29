class Pub:
    def __init__(self, _pub_name, _till):
        self.name = _pub_name
        self.till = _till
        self.customers = []
        self.drink = []
    
    def increase_till(self, amount):
        self.till += amount

    def add_customer_to_pub(self, customer):
        self.customers.append(customer)

    
    def sell_drink_to_customer(self, customer, drink):
        pass
    # add drink to customer, remove the price of drink
    # add price of drink to till
    # reduce stock
    
    
    