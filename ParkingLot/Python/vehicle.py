from spotType import SpotType
class Vehicle:
    def __init__(self, license_plate: str, spot_type: SpotType):
        self.license_plate = license_plate
        self.spot_type = spot_type
    
    def __str__(self):
        return (f"Vehicle {self.license_plate} [{self.spot_type}]")