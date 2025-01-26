from vendingmachine import VendingMachine
from product import Product
from money import Money
from moneytype import MoneyType

#instantiate machine
machine = VendingMachine('abc@gmail.com')

#load change into machine
machine.payment_processor.add_change(Money(0.10, MoneyType.COIN), 10)
machine.payment_processor.add_change(Money(0.25, MoneyType.COIN), 10)
machine.payment_processor.add_change(Money(1.00, MoneyType.BILL), 10)

#define products
Pepsi = Product(1, 'Pepsi', 1.50)
Cola = Product(2, 'Cola', 2.00)
Lays = Product(3, 'Lays', 3.00)
Chocoloate = Product(3, 'Five Star', 3.75)

#load products to inventory
machine.inventory.add_product(Pepsi, 1, 10)
machine.inventory.add_product(Cola, 2, 5)
machine.inventory.add_product(Lays, 3, 10)
machine.inventory.add_product(Chocoloate, 4, 10)

#select product on the machine using aisle Id
machine.select_product(1)

#user inserts money coin/bills one by one in the machine
money = Money(1.25, MoneyType.BILL)
machine.insert_money(money)


#tries to dispense product
machine.dispense_product()

print(machine.inventory)
print(machine.payment_processor.get_current_balance())


