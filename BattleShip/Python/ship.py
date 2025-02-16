class Ship:
    def __init__(self, ship_id, length):
        self.ship_id = ship_id
        self.length = length
        self.coordinates = set()
        self.hits = set()

    def is_sunk(self):
        return len(self.hits) == self.length
        
