from board import Board
from symbol import Symbol

class WinChecker:
    @staticmethod
    def check_winner(board: Board, symbol: Symbol):
        size = board.size
        #check rows and columns
        
        for i in range(size):
            if all(board.grid[i][j] == symbol.value for j in range(size)) or all(board.grid[j][i] == symbol.value for j in range(size)):
                return True
        
        #check diagonals
        if all(board.grid[i][i] == symbol.value for i in range(size)) or all(board.grid[i][size - i - 1] == symbol.value for i in range(size)):
            return True
        
        #return false if both conditions are not winning
        return False
        
        




        

