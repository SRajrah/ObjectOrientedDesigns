from product import Product
class Inventory:
    def __init__(self):
        self.__product_stock = {}
    
    def add_product(self, product, qty: int):
        if product in self.__product_stock:
            self.__product_stock[product]  += qty
        else:
            self.__product_stock[product]  = qty
    
    def reduce_product_qty(self, product, qty: int = 1):
        if product in self.__product_stock and self.__product_stock[product] >= qty:
            self.__product_stock[product] -= qty
        else:
            raise ValueError("Insufficient stock or product not found. Sorry for the inconvenience. Owner has been notified!")

    def is_product_available(self, product):
        return product in self.__product_stock and self.__product_stock[product] > 0

    def get_product_qty(self, product):
        return self.__product_stock.get(product, 0)
    
    def __str__(self):
        return "\n".join(
            [f"{product.get_name()}: {quantity}" for product, quantity in self.__product_stock.items()]
        )


#EXAMPLE
# # Create Product instances
# product1 = Product(1, "Soda", 1.50)
# product2 = Product(2, "Chips", 2.00)
# product3 = Product(3, "Candy", 1.25)

# # Create Inventory instance
# inventory = Inventory()

# # Add products to inventory
# inventory.add_product(product1, 10)
# inventory.add_product(product2, 5)
# inventory.add_product(product3, 8)

# # Print inventory
# print("Initial Inventory:")
# print(inventory)

# # Reduce stock
# inventory.reduce_product_qty(product1, 2)
# print("\nAfter selling 2 Sodas:")
# print(inventory)

# # Check availability
# print("\nIs Chips available?", inventory.is_product_available(product2))

# # Get quantity of a specific product
# print("Candy stock:", inventory.get_product_qty(product3))