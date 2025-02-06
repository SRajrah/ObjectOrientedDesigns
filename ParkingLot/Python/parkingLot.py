from parkingFloor import ParkingFloor
from parkingTicket import ParkingTicket
from datetime import datetime
import threading
from paymentProcessorFactory import PaymentProcessorFactory

class ParkingLot:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, name, floors):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ParkingLot, cls).__new__(cls)
                cls._instance.init_parking_lot(name, floors)
        return cls._instance
    
    def init_parking_lot(self, name: str, floors: ParkingFloor):
        self.name = name
        self.floors = floors
        self.occupied_spots = {}
        self.ticket_counter = 0
        self.payment_processor = PaymentProcessorFactory.get_processor("Card")
    
    def assign_spot(self, vehicle):
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle.spot_type)
            if spot:
                spot.park_vehicle(vehicle)
                self.ticket_counter += 1
                ticket = ParkingTicket(self.ticket_counter, vehicle, spot)
                self.occupied_spots[vehicle.license_plate] = (spot, ticket)
                print(f"Vehicle {vehicle.license_plate} parked at Spot : {spot.spot_id} on Floor : {floor.floor_number}")
                return ticket
        print(f"No Spot Available")
        return None
    
    def release_spot(self, vehicle):
        if vehicle.license_plate in self.occupied_spots:
            spot, ticket = self.occupied_spots[vehicle.license_plate]
            
            for floor in self.floors:
                if floor.floor_number == spot.floor_number:
                    spot.vehicle = None
                    spot.is_available = True
                    del self.occupied_spots[vehicle.license_plate]
                    floor.release_spot(spot)
                    ticket.exit_time = datetime.now()
                    print(f'Vehicle {vehicle.license_plate} removed from Spot: {spot.spot_id} on Floor {spot.floor_number}.')
                    return ticket

        print(f"Vehicle {vehicle.license_plate} not found in the parking lot.")
        return None

