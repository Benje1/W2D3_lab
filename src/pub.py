class Pub:
    def __init__(self, _pub_name, _till):
        self.name = _pub_name
        self.till = _till
        self.customer = []
    
    def increase_till(self, amount):
        self.till += amount

    def add_customer_to_pub(self, customer):
        self.customer.append(customer)

    def sell_drink_to_customer(self, amount):
        self.increase_till(amount)
        self.customer.reduce_wallet(amount)

    
    
    
    