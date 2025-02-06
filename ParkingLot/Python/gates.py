
import threading
from paymentScreen import PaymentScreen
from parkingLot import ParkingLot
from vehicle import Vehicle
class EntranceGate:
    def __init__(self, gate_id: int, parking_lot: ParkingLot):
        self.gate_id = gate_id
        self.parking_lot = parking_lot
        self.lock = threading.Lock()

    def enter_parking(self, vehicle: Vehicle):
        with self.lock:
            print(f"Vehicle {vehicle.license_plate} entering through Gate {self.gate_id}")
            ticket = self.parking_lot.assign_spot(vehicle)
            return ticket

class ExitGate:
    def __init__(self, gate_id : int, parking_lot: ParkingLot, payment_screen: PaymentScreen):
        self.gate_id = gate_id
        self.parking_lot = parking_lot
        self.payment_screen = payment_screen
        self.lock = threading.Lock()
    
    def exit_parking(self, vehicle: Vehicle):
        with self.lock:
            print(f"Vehicle {vehicle.license_plate} exiting through Gate {self.gate_id}")
            ticket = self.parking_lot.release_spot(vehicle)
            if ticket:
                self.payment_screen.notify(ticket, self)
                return ticket
    def update(self, ticket):
        if ticket.is_paid:
            print(f"Exit Gate {self.gate_id}: Payment verified for Vehicle {ticket.vehicle.license_plate}. You may exit.")
        else:
            print(f"Exit Gate {self.gate_id}: Payment pending for Vehicle {ticket.vehicle.license_plate}. Please pay first.")
