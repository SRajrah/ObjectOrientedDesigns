from symbol import Symbol
from moveStrategy import MoveStrategy
class Player:
    def __init__(self, name : str, symbol: Symbol, strategy: MoveStrategy):
        self.name = name
        self.symbol = symbol
        self.strategy = strategy
    
    def make_move(self, board):
        return self.strategy.get_move(board)

    def __str__(self):
        return self.name
    