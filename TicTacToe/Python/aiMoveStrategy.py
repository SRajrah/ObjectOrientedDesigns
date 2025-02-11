
from moveStrategy import MoveStrategy
import random

class AIMoveStrategy(MoveStrategy):
    def get_move(self, board):
        available_moves =[(r, c) for r in range(board.size) for c in range(board.size) if board.is_cell_empty(r, c)]
        return random.choice(available_moves) if available_moves else (-1, -1)
    