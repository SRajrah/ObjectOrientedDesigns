from moneytype import MoneyType
class Money:
    def __init__(self, value, money_type: MoneyType):
        if value <= 0:
            raise ValueError("Money Value should be positive.")
        self.__value = value
        self.__money_type = money_type
    
    def get_value(self):
        return self.__value

    def get_money_type(self):
        return self.__money_type

    def __str__(self):
        return f"{self.__money_type.value} (${self.__value:.2f})"
    

# Create Money instances
coin = Money(0.25, MoneyType.COIN)
bill = Money(1.00, MoneyType.BILL)

# Display the money details
print(coin)  # Output: Coin($0.25)
print(bill)  # Output: Bill($1.00)

# Access the attributes
print("Coin value:", coin.get_value())  # Output: 0.25
print("Bill type:", bill.get_money_type())  # Output: MoneyType.BILL
