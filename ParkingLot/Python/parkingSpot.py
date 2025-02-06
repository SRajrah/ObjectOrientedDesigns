from spotType import SpotType
class ParkingSpot:
    def __init__(self, spot_id : int, spot_type : SpotType, lift_distance : int, floor_number: int):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.lift_distance = lift_distance
        self.vehicle = None
        self.is_available = True
        self.floor_number = floor_number
    
    def park_vehicle(self, vehicle):
        if self.is_available:
            self.vehicle = vehicle
            self.is_available = False
            return True
        return False
    
    def remove_vehicle(self):
        if not self.is_available:
            self.vehicle = None
            self.is_available = True
            return True
        return False
    
    def __str__(self):
        status = "Available" if self.is_available else f"Occupied by {self.vehicle.license_plate}"
        return f"Spot {self.spot_id} [{self.spot_type.name}] - {status}"


