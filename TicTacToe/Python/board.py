from player import Player
from symbol import Symbol
class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
    
    # def display(self):
    #     for row in self.grid:
    #         print(" | ".join(row))
    #         print("-" * (self.size * 4 - 1))
    def display(self):
        size = self.size
        border = "┌" + "───┬" * (size - 1) + "───┐"  # Top border
        separator = "├" + "───┼" * (size - 1) + "───┤"  # Middle separator
        bottom = "└" + "───┴" * (size - 1) + "───┘"  # Bottom border

        print(border)  # Print top border

        for i in range(size):
            print("│ " + " │ ".join(self.grid[i]) + " │")  # Print row with borders
            if i < size - 1:
                print(separator)  # Print separator between rows

        print(bottom)  # Print bottom border
    
    def is_cell_empty(self, row : int, col : int):
        return self.grid[row][col] == ' '

    def mark_cell(self, row : int, col : int, symbol: Symbol):
        if self.is_cell_empty(row, col):
            self.grid[row][col] = symbol.value
            return True
        return False
    
    def is_full(self):
        return all(self.grid[row][col] != ' ' for row in range(self.size) for col in range(self.size) )
        
