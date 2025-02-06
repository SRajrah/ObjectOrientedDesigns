from datetime import datetime, timedelta

class ParkingTicket:
    def __init__(self, ticket_id: int, vehicle, spot, rate_per_hour = 5):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.rate_per_hour = rate_per_hour
        self.entry_time = datetime.now()
        self.exit_tine = None
        self.amount_due = 0
        self.is_paid = False
    
    def calculate_amount_due(self):
        if self.exit_tine is None:
            self.exit_time = datetime.now()
        duration = (self.exit_time - self.entry_time).total_seconds() / 3600
        self.amount_due = round(duration * self.rate_per_hour, 2)
        return self.amount_due

    def mark_paid(self):
        self.is_paid = True
        print(f"Ticket {self.ticket_id} is paid. Amount : {self.amount_due}")
    
    def __str__(self):
        print(f"Ticket Id :{self.ticket_id}, Vehicle : {self.vehicle.license_plate}, Spot : {self.spot.spot_id}, Paid : {self.is_paid}")
     