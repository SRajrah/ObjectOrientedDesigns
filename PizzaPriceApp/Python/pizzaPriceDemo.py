# Creating a predefined pizza
from predefinedPizza import PredefinedPizza
from customPizza import CustomPizza
from enums import Size, CrustType, ToppingType
from topping import Topping
from decorators import ExtraCheeseDecorator
from discounts import PercentageDiscount, FixedAmountDiscount

margherita = PredefinedPizza("Margherita") #factory
margherita.add_topping(Topping("Olives", 1.2, ToppingType.VEGAN))
print(margherita)
print("Price: $", margherita.calculate_price())
margherita.set_discount(FixedAmountDiscount(10))
print("Price after discount : $", margherita.calculate_price())


# Creating a custom pizza
custom_pizza = CustomPizza(Size.LARGE, CrustType.GLUTEN_FREE)
custom_pizza.add_topping(Topping("Cheese", 2.0, ToppingType.VEG))
custom_pizza.add_topping(Topping("Olives", 1.2, ToppingType.VEGAN))
print(custom_pizza)
print("Price: $", custom_pizza.calculate_price())

# Applying Extra Cheese Decorator
extra_cheese_pizza = ExtraCheeseDecorator(custom_pizza)
print(extra_cheese_pizza)
print("Price with Extra Cheese: $", extra_cheese_pizza.calculate_price())