from symbol import Symbol
class Player:
    def __init__(self, name : str, symbol: Symbol):
        self.name = name
        self.symbol = symbol
    def __str__(self):
        return self.name
    