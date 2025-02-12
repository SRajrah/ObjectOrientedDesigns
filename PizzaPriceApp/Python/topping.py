from enums import ToppingType
class Topping:
    def __init__(self, name : str, price : float, topping_type: ToppingType):
        self.name = name
        self.price = price
        self.topping_type = topping_type
    
    def __str__(self):
        return  f"{self.name} ( ${self.price}, {self.topping_type.value})"
