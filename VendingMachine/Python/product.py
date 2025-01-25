class Product:
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price


#EXAMPLE
# Create a product instance
# product = Product(1, "Soda", 1.50)

# Access attributes using getters
# print(product.get_id())  # Output: 1
# print(product.get_name())        # Output: Soda
# print(product.get_price())       # Output: 1.5

# Attempting to access private attributes directly
# print(product.__price)  # Raises AttributeError
    