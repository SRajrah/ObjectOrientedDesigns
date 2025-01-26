from paymentprocessor import PaymentProcessor
from money import Money
from moneytype import MoneyType

processor = PaymentProcessor()

#add change to processor
processor.add_change(Money(0.10, MoneyType.COIN), 10)
processor.add_change(Money(0.25, MoneyType.COIN), 10)
processor.add_change(Money(1.00, MoneyType.BILL), 10)


#accept money
processor.accept_payment(Money(0.25, MoneyType.COIN))
processor.accept_payment(Money(1.00, MoneyType.COIN))

print(f"Current balance : {processor.get_current_balance()}")

change = processor.calculate_change(1.00)

if change:
    print("Change retured : ")
    for money in change:
        print(money)

# Refund balance
print("Refunded amount:", processor.refund_amount())

# Display available change in machine
print("Change available in machine:", processor.get_available_change())
print(f"Current balance : {processor.get_current_balance()}")
