from pizza import Pizza
class ExtraCheeseDecorator(Pizza):
    def __init__(self, pizza : Pizza):
        self.pizza = pizza
    
    def calculate_price(self):
        return self.pizza.calculate_price() + 2.0
    
    def __getattr__(self, attr):
        return getattr(self.pizza, attr)
    
    def __str__(self):
        return f"{self.pizza} + Extra Cheese"
        