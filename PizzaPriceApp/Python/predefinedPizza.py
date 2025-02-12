from pizza import Pizza
from topping import Topping
from enums import Size, CrustType, ToppingType

class PredefinedPizza(Pizza):
    PREDEFINED_PIZZAS = {
        "Margherita": {"crust": CrustType.THIN, "size": Size.MEDIUM, "toppings": [Topping("Cheese", 2.0, ToppingType.VEG)]},
        "Pepperoni": {"crust": CrustType.THICK, "size": Size.LARGE, "toppings": [Topping("Cheese", 2.0, ToppingType.VEG), Topping("Pepperoni", 3.0, ToppingType.NON_VEG)]},
    }


    def __init__(self, name : str):
        if name not in self.PREDEFINED_PIZZAS:
            raise ValueError(f"Predefined {name} does not exist.")
        
        pizza_data = self.PREDEFINED_PIZZAS[name]
        super().__init__(name, pizza_data['size'], pizza_data['crust'])

        self.toppings = pizza_data['toppings']
