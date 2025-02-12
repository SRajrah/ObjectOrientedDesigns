from enums import Size, CrustType
from topping import Topping
from abc import ABC, abstractmethod
from discountStrategy import DiscountStrategy
from discounts import NoDiscount

class Pizza(ABC):
    def __init__(self, name: str, size: Size, crust: CrustType, discount_strategy: DiscountStrategy = NoDiscount()):
        self.name = name
        self.size = size
        self.crust = crust
        self.toppings = []
        self.discount_strategy = discount_strategy
    
    def add_topping(self, topping : Topping):
        self.toppings.append(topping)
    
    def get_toppings(self):
        return [topping.name for topping in self.toppings]
    
    def set_discount(self, discount_strategy: DiscountStrategy):
        """Allows setting a discount dynamically."""
        self.discount_strategy = discount_strategy
    
    def calculate_price(self):
        base_price = self.crust.value  # Crust price
        topping_price = sum(t.price for t in self.toppings)  # Sum of all toppings
        total_price = (base_price + topping_price) * self.size.value
        return round(self.discount_strategy.apply_discount(total_price), 2) # Apply size multiplier

    def __str__(self):
        return f"{self.name} ({self.size.name}, {self.crust.name}) with toppings: {', '.join(self.get_toppings())}"
    
