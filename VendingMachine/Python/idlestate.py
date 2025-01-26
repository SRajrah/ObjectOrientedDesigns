from vendingmachinestate import VendingMachineState
from product import Product

class IdleState(VendingMachineState):
    def __init__(self, machine):
        self.__machine = machine
    
    def select_product(self, aisle_id: int):
        self.__machine.display.show_message(f"Product at {aisle_id} selected.")
        self.__machine.set_selected_product(aisle_id)
        self.__machine.set_state(self.__machine.processing_state)
    
    def insert_money(self, money):
        self.__machine.display.show_message(f'Please select a product first.')
    
    def dispense_product(self):
        self.__machine.display.show_message(f'No Product Selected.')
    
    def cancel_transaction(self):
        self.__machine.display.show_message(f'No transaction to cancel.')