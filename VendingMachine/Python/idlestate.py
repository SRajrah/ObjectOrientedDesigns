from vendingmachinestate import VendingMachineState

class IdleState(VendingMachineState):
    def __init__(self, machine):
        self.__machine = machine
    
    def select_product(self, id):
        print(f'Product: {id} selected')
        self.__machine.set_selected_product(id)
        self.__machine.set_state(self.__machine.processing_state)
    
    def insert_money(self, money):
        print(f'Please select a product first.')
    
    def dispense_product(self):
        print(f'No Product Selected.')
    
    def cancel_transaction(self):
        print(f'No transaction to cancel.')