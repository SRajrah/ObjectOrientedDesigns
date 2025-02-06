from datetime import datetime
import threading
from parkingFloor import ParkingFloor
from parkingSpot import ParkingSpot
from parkingLot import ParkingLot
from spotType import SpotType
from gates import EntranceGate, ExitGate
from paymentScreen import PaymentScreen
from vehicle import Vehicle

floor_1 = ParkingFloor( 1, 
    [
        ParkingSpot(1, SpotType.MOTORBIKE, 10, 1),
        ParkingSpot(2, SpotType.COMPACT, 20, 1),
        ParkingSpot(3, SpotType.COMPACT, 20, 1),
        ParkingSpot(4, SpotType.ACCESSIBLE, 20, 1),
    ]
)

parking_lot = ParkingLot("Rajrah Parking", [floor_1])

paymentScreen = PaymentScreen()
entrance_gate_1 = EntranceGate(1, parking_lot)
entrance_gate_2 = EntranceGate(2, parking_lot)
exit_gate_1 = ExitGate(1, parking_lot, paymentScreen)
exit_gate_2 = ExitGate(2, parking_lot, paymentScreen)

paymentScreen.attach(exit_gate_1)
paymentScreen.attach(exit_gate_2)

vehicle_1 = Vehicle("123-ABC", SpotType.MOTORBIKE)
vehicle_2 = Vehicle("456-DEF", SpotType.COMPACT)


ticket_1 = entrance_gate_1.enter_parking(vehicle_1)
ticket_2 = entrance_gate_2.enter_parking(vehicle_2)

ticket_1.exit_time = datetime.now()
ticket_1_amount_paid = 1
parking_lot.payment_processor.process_payment(ticket_1, ticket_1_amount_paid)

ticket_1 = exit_gate_1.exit_parking(vehicle_1)
ticket_2 = exit_gate_2.exit_parking(vehicle_2)

