import heapq
from spotType import SpotType

class ParkingFloor:
    def __init__(self, floor_number: int, spots):
        self.floor_number = floor_number
        self.spots = spots
        self.spot_heaps = {spot_type: [] for spot_type in SpotType}
        self.heap_entry_id = 1
        self.arrangeSpots(spots)
        
    
    def arrangeSpots(self, spots):
        for spot in spots:
            heapq.heappush(self.spot_heaps[spot.spot_type], (spot.lift_distance, self.heap_entry_id, spot))
            self.heap_entry_id += 1


    def find_available_spot(self, spot_type):
        if self.spot_heaps[spot_type]:
            return heapq.heappop(self.spot_heaps[spot_type])[2]
    
    def release_spot(self, spot):
        heapq.heappush(self.spot_heaps[spot.spot_type], (spot.lift_distance, self.heap_entry_id, spot))
        self.heap_entry_id += 1



    def __str__(self):
        return f"Floor : {self.floor_number} has {len(self.spots) } Spots."