from parkingTicket import ParkingTicket
class PaymentProcessorFactory:
    @staticmethod
    def get_processor(payment_method):
        if payment_method == 'Card':
            return CardPaymentProcessor()
        if payment_method == 'UPI':
            return UpiPaymentProcessor()


class PaymentProcessor:
    def process_payment(self, ticket : ParkingTicket, amount: int):
        pass

class CardPaymentProcessor(PaymentProcessor):
    def __init__(self):
            self.transactions = []  # Store successful transactions

    def process_payment(self, ticket: ParkingTicket, amount: float):

        due = ticket.calculate_amount_due()
        print(f"Processing Card Payment for Ticket {ticket.ticket_id}, Due :{due} and Amount: ${amount}")

        if amount < due:
            print(f"Payment Failed! Amount ${amount} is less than due: ${due}.")
            return False

        ticket.mark_paid()
        ticket.amount_due = 0  
        self.transactions.append((ticket.ticket_id, amount)) 
        print(f'Payment Successful! Vehicle {ticket.vehicle.license_plate} paid ${amount} via Card')
        return True

        

class UpiPaymentProcessor(PaymentProcessor):
    def process_payment(self, ticket, amount):
        print(f"Processing Card Payment for Ticket {ticket.ticket_id}, Amount: ${amount}")
        ticket.mark_paid()