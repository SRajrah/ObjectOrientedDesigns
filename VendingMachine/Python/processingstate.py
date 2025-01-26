from vendingmachinestate import VendingMachineState
from product import Product
class ProcessingState(VendingMachineState):
    def __init__(self, machine):
        self.__machine = machine
    
    def select_product(self, aisle_id : int):
        self.__machine.display.show_message(f'A product is already selected.')
    
    def insert_money(self, money):
        self.__machine.display.show_message(f'Inserted Money: {money}.')
        self.__machine.payment_processor.accept_payment(money)

        if self.__machine.payment_processor.get_current_balance() >= self.__machine.get_selected_product_price():
            self.__machine.set_state(self.__machine.dispensing_state)
    
    def dispense_product(self):
        self.__machine.display.show_message(f'Insufficient Payment, please insert more money.')
    
    def cancel_transaction(self):
       self.__machine.display.show_message('Transaction cancelled. Refunding money.')
       self.__machine.payment_processor.refund_amount()
       self.__machine.set_state(self.__machine.idle_state) 