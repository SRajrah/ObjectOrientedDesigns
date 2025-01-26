from moneytype import MoneyType
from money import Money

class PaymentProcessor:
    def __init__(self):
        self.__current_balance = 0.0

        #accepted denominations
        self.__accepted_denominations = {
            0.05 : Money(0.05, MoneyType.COIN),
            0.10 : Money(0.10, MoneyType.COIN),
            0.25 : Money(0.25, MoneyType.COIN),
            1.00 : Money(1.00, MoneyType.BILL),
            5.00 : Money(5.00, MoneyType.BILL),
            10.00 : Money(10.00, MoneyType.BILL)
        }

        #change storage : money value -> quantity
        self.__change_available = {}

    #accept payment if denom valid
    def accept_payment(self, money: Money):
        if money.get_value() in self.__accepted_denominations:
            self.__current_balance += money.get_value()
        else:
            self.display.show_message(f"Rejected : {money}")
    
    #calculate and dispense change
    def calculate_change(self, amount: float):
        if self.__current_balance < amount:
            self.display.show_message(f"Insufficient funds. Please add more money : ${amount - self.__current_balance}")
            self.refund_amount()
            return None
        
        change_given = []
        change_to_return = self.__current_balance - amount
        
        if change_to_return == 0:
            return change_given
        
        if change_to_return >  sum([val * qty for val, qty in self.__change_available.items()]):
            self.display.show_message("Machine low on change.")
            self.notification.send_notification("Machine is low in change. Please refill change.")
            self.refund_amount()
            return None
        
        for value in sorted(self.__change_available.keys(), reverse = True):
            while change_to_return >= value and self.__change_available[value] > 0:
                change_to_return -= value
                self.__change_available[value] -= 1
                change_given.append(Money(value, self.__accepted_denominations[value].get_money_type()))
        
        if change_to_return > 0:
            self.display.show_message("Unable to return exact change.")
            self.refund_amount()
            self.notification.send_notification("Machine is low on change. Please refill change.")
            return None

        self.__current_balance = 0
        return change_given

    def refund_amount(self):
        refunded_amount = self.__current_balance
        self.__current_balance = 0.0
        self.display.show_message(f'Amount refunded: {refunded_amount}')
        return refunded_amount
    
    def get_current_balance(self):
        return self.__current_balance

    def add_change(self, money : Money, quantity: int):
        if money.get_value() in self.__accepted_denominations:
            if money.get_value() in self.__change_available:
                self.__change_available[money.get_value()] += quantity
            else:
                self.__change_available[money.get_value()] = quantity
        else:
            self.display.show_message(f"{money.get_value()} not an accepted denomination.")
    
    def get_available_change(self):
        return self.__change_available

    def __str__(self):
        return f"Current balance: ${self.__current_balance:.2f}"


