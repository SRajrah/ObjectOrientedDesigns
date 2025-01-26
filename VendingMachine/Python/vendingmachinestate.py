from abc import ABC, abstractmethod
from money import Money
from product import Product
class VendingMachineState(ABC):
    @abstractmethod
    def select_product(self, product: Product):
        pass

    @abstractmethod
    def insert_money(self, money: Money):
        pass

    @abstractmethod
    def dispense_product(self):
        pass    
    
    @abstractmethod
    def cancel_transaction(self):
        pass