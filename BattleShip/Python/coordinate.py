class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def is_valid(self, board = 10):
        return  0 <= self.x < board and 0 <= self.y < board
    
    def __eq__(self, other):
        return isinstance(other, Coordinate) and self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))


    