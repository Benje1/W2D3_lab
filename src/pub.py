class Pub:
    def __init__(self, _pub_name, _till):
        self.name = _pub_name
        self.till = _till
        self.customers = []
        self.stock = {}
    
    def increase_till(self, amount):
        self.till += amount

    def add_customer_to_pub(self, customer):
        self.customers.append(customer)

    
    def sell_drink_to_customer(self, customer, drink):
        if customer.age >= 18 and customer.alcohol_level < 5:
            if self.check_stock_level(drink) > 0:
                customer.buy_drink(drink)
                self.increase_till(drink.price)
    
    def sell_food_to_customer(self, customer, food):
        customer.buy_food(food)
        self.increase_till(food.price)
    
    def add_drink(self, drink):
        if drink in self.stock:
            self.stock[drink] += 3
        else:
            self.stock[drink] = 3
    
    def check_stock_level(self, drink):
        if drink in self.stock:
            return self.stock[drink]
        else:
            return 0
    
    def check_stock_total_value(self, drink):
        total_value = 0
        for drink in self.stock:
            total_value += drink.price * self.stock[drink]
        return total_value

