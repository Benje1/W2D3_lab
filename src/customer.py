class Customer:
    def __init__(self, _name, _wallet, _age):
        self.name = _name
        self.wallet = _wallet
        self.age = _age
        self.drunkeness = 0

    def reduce_wallet(self, amount):
        self.wallet -= amount