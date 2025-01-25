from vendingmachinestate import VendingMachineState

class OutOfServiceState(VendingMachineState):
    def __init__(self, machine):
        self.__machine = machine
    
    def select_product(self, id):
        print('Machine is out of service. Sorry for the inconvenience.')
    def insert_money(self, money):
        print('Machine is out of service. Sorry for the inconvenience.')
    def dispense_product(self):
        print('Machine is out of service. Sorry for the inconvenience.')
    def cancel_transaction(self):
        print('Machine is out of service. Sorry for the inconvenience.')