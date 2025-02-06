class PaymentScreen:
    def __init__(self):
        self.observers = []
    
    def attach(self, observer):
        self.observers.append(observer)
    
    def notify(self, ticket, exit_date):
        exit_date.update(ticket)
