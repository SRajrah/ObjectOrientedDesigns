from vendingmachinestate import VendingMachineState
from inventory import Inventory

class DispensingState(VendingMachineState):
    def __init__(self, machine):
       self.__machine = machine
    
    def select_product(self, aisle_id: int):
        self.__machine.display.show_message(f'Cannot select a product while dispensing.')
    
    def insert_money(self, money):
        self.__machine.display.show_message(f'Cannot insert money while dispensing.')
    
    def dispense_product(self):
        self.__machine.display.show_message(f'Dispensing product : {self.__machine.get_selected_product().get_name()} Process Started ...')
        change = self.__machine.payment_processor.calculate_change(self.__machine.get_selected_product_price())
        
        if change and len(change) >= 0:
            self.__machine.display.show_message(f'Returning Change: {list(map(str, change))}')
            self.__machine.inventory.reduce_product_qty(self.__machine.get_selected_product())
            self.__machine.display.show_message(f'Dispensing product : {self.__machine.get_selected_product().get_name()} Process Complete ...')
        else:
            self.__machine.display.show_message(f'Dispensing product : {self.__machine.get_selected_product().get_name()} Process Failed ...')
        
        self.__machine.set_state(self.__machine.idle_state)
    
    def cancel_transaction(self):
        self.__machine.display.show_message(f'Cannot cancel while dispensing.')