class Customer:
    def __init__(self, _name, _wallet, _age):
        self.name = _name
        self.wallet = _wallet
        self.age = _age
        self.drinks = []
        self.alcohol_level = 0

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def buy_drink(self, drink):
        self.drinks.append(drink)
        self.reduce_wallet(drink.price)
        self.alcohol_level += drink.alcohol_level

    def buy_food(self, food):
        self.reduce_wallet(food.price)
        self.alcohol_level -= food.rejuvenation_level
