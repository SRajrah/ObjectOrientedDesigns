from ship import Ship
from coordinate import Coordinate
class board:
    def __init__(self, size = 10):
        self.size = size
        self.grid = [['.' for _ in range(self.size)] for _ in range(self.size)]
        self.ships = {}

    def place_ship(self, ship: Ship, start_coord: Coordinate, direction: str):
        coords = []
        if not start_coord.is_valid:
            raise ValueError("Start Location is Invalid")
        
        for i in range(ship.length):
            x, y = start_coord.x, start_coord.y
            if direction == 'up':
                x -= 1
            elif direction == 'down':
                x += 1
            elif direction == 'right':
                y += 1
            elif direction == 'left':
                y -= 1
            else:
                raise ValueError("Invalid Direction Given!")
            
            coord = Coordinate(x, y)
            if not coord.is_valid(self.size) or self.grid[x][y] != '.':
                return False
            coords.append(coord)

        for coord in coords:
            self.grid[coord.x][coord.y]  = ship.ship_id
            ship.coordinates.add(coord) 
        
        self.ships[ship.ship_id] = ship
        return True
    
    def receive_attack(self, coord: Coordinate):
        if not coord.is_valid(self.size):
            return "Invalid Location Selected."

        cell = self.grid[coord.x][coord.y]
        if cell == 'O' or cell == '.':
            pass


        


