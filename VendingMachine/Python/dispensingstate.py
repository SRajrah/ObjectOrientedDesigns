from vendingmachinestate import VendingMachineState
from inventory import Inventory

class DispensingState(VendingMachineState):
    def __init__(self, machine):
       self.__machine = machine
    
    def select_product(self, id):
        print(f'Cannot select a product while dispensing.')
    
    def insert_money(self, money):
        print(f'Cannot insert money while dispensing.')
    
    def dispense_product(self):
        print(f'Dispensing product : {self.__machine.get_selected_product().get_name()}')
        self.__machine.inventory.reduce_product_qty(self.__machine.get_selected_product())
        change = self.__machine.payment_processor.calculate_change(self.__machine.get_selected_product_price())
        if change:
            print('Returning Change: {change}')
        self.__machine.set_state(self.__machine.idle_state)
    
    def cancel_transaction(self):
        print(f'Cannot cancel while dispensing.')