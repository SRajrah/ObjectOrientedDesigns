from idlestate import IdleState
from processingstate import ProcessingState
from dispensingstate import DispensingState
from outofservicestate import OutOfServiceState
from inventory import Inventory
from vendingmachinestate import VendingMachineState
from money import Money
from product import Product
from paymentprocessor import PaymentProcessor
from display import Display
from notification import Notification
class VendingMachine:
    __instance = None
    def __new__(cls, owner_contact):
        if cls.__instance is None:
            cls.__instance = super(VendingMachine, cls).__new__(cls)
        return cls.__instance
   
    def __init__(self, owner_contact):
        if not hasattr(self, "_initialzied"):
            self._initialzed = True

            #initialize the states
            self.idle_state = IdleState(self)
            self.processing_state = ProcessingState(self)
            self.dispensing_state = DispensingState(self)
            self.out_of_service_state = OutOfServiceState(self)
            self.current_state = self.idle_state

            #core components
            self.display = Display()
            self.notification = Notification(owner_contact)
            self.inventory = Inventory()
            self.payment_processor = PaymentProcessor(self)
            self.selected_product =  None

    def set_state(self, state: VendingMachineState):
        self.current_state = state
    
    def get_state(self) -> VendingMachineState:
        return self.current_state

    #product selection methods
    def select_product(self, aisle_id: int):
        self.current_state.select_product(aisle_id)
    
    #money insertion method
    def insert_money(self, money: Money):
        self.current_state.insert_money(money)

    #dispense product method
    def dispense_product(self):
        self.current_state.dispense_product()

    def cancel_transaction(self):
        self.current_state.cancel_transaction()
    

    #set selected product details
    def set_selected_product(self, aisle_id: int):
        product = self.inventory.get_product(aisle_id)
        self.selected_product = product
    
    def get_selected_product(self) -> Product:
        return self.selected_product

    def get_selected_product_price(self) -> Product:
        return self.selected_product.get_price()