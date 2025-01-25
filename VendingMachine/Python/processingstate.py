from vendingmachinestate import VendingMachineState

class ProcessingState(VendingMachineState):
    def __init__(self, machine):
        self.__machine = machine
    
    def select_product(self, id):
        print(f'A product is already selected.')
    
    def insert_money(self, money):
        print(f'Inserted Money: {money}.')
        self.__machine.payment_processor.accept_money(money)

        if self.__machine.payment_processor.get_current_balance() >= self.__machine.get_selected_product_price():
            self.__machine.set_state(self.__machine.dispensing_state)
    
    def dispense_product(self):
        print(f'Insufficient Payment, please insert more money.')
    
    def cancel_transaction(self):
       print('Transaction cancelled. Refunding money.')
       self.__machine.payment_processor.refund_amount()
       self.__machine.set_state(self.__machine.idle_state) 