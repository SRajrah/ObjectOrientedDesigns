from pizza import Pizza
from enums import Size, CrustType

class CustomPizza(Pizza):
    def __init__(self,size: Size, crust: CrustType):
        super().__init__("Custom Pizza", size, crust)