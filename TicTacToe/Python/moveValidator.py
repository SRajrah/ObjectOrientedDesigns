from board import Board
class MoveValidator:
    @staticmethod
    def is_valid_move(board : Board, row : int, col : int):
        if board.is_cell_empty(row, col) and 0 <= row < board.size and 0 <= col < board.size:
            return True
        return False