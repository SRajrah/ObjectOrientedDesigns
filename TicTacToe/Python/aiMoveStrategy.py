
from moveStrategy import MoveStrategy
import random
import time

class AIMoveStrategy(MoveStrategy):
    def get_move(self, board):
        print("Thinking Move....")
        time.sleep(2)
        available_moves =[(r, c) for r in range(board.size) for c in range(board.size) if board.is_cell_empty(r, c)]
        return random.choice(available_moves) if available_moves else (-1, -1)
    