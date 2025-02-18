from abc import ABC, abstractmethod
import time
from threading import Lock

# ---------------------------------------------------------------------------------------
# 1. Singleton Pattern (Ensures only one ATM instance per machine)
# ---------------------------------------------------------------------------------------
class SingletonMeta(type):
    """
    Singleton MetaClass ensures that only one ATM instance exists.
    """
    _instances = {}
    _lock = Lock()  # Thread-safe implementation

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# ---------------------------------------------------------------------------------------
# 2. State Pattern (ATM has different states: Idle, Authenticating, Processing)
# ---------------------------------------------------------------------------------------
class ATMState(ABC):
    """
    Abstract base class representing ATM states.
    """
    @abstractmethod
    def insert_card(self, atm, card, pin): pass

    @abstractmethod
    def eject_card(self, atm): pass

    @abstractmethod
    def perform_transaction(self, atm, strategy, amount): pass

# Concrete States
class IdleState(ATMState):
    def insert_card(self, atm, card, pin):
        if card.linked_account.authenticate(pin):
            atm.current_card = card
            atm.change_state(ProcessingState())
            print("Authentication successful. ATM ready for transactions.")
        else:
            print("Invalid PIN. Please try again.")

    def eject_card(self, atm):
        print("No card inserted.")

    def perform_transaction(self, atm, strategy, amount):
        print("Please insert a card first.")

class ProcessingState(ATMState):
    def insert_card(self, atm, card, pin):
        print("Card already inserted.")

    def eject_card(self, atm):
        print("Card ejected.")
        atm.current_card = None
        atm.change_state(IdleState())

    def perform_transaction(self, atm, strategy, amount):
        if not atm.current_card:
            print("No card inserted.")
            return
        if strategy.execute(atm.current_card.linked_account, atm.cash_dispenser, amount):
            transaction = TransactionFactory.create_transaction(atm.current_card.linked_account, strategy.__class__.__name__, amount)
            atm.notify_observers(transaction)  # Notify observers about the transaction

# ---------------------------------------------------------------------------------------
# 3. Strategy Pattern (For different transaction types)
# ---------------------------------------------------------------------------------------
class TransactionStrategy(ABC):
    """
    Strategy interface for different transaction types.
    """
    @abstractmethod
    def execute(self, account, cash_dispenser, amount): pass

class WithdrawStrategy(TransactionStrategy):
    def execute(self, account, cash_dispenser, amount):
        if account.withdraw(amount) and cash_dispenser.dispense_cash(amount):
            print(f"Withdrawal successful. New Balance: ${account.get_balance():.2f}")
            return True
        print("Insufficient funds or ATM cash unavailable.")
        return False

class DepositStrategy(TransactionStrategy):
    def execute(self, account, cash_dispenser, amount):
        account.deposit(amount)
        cash_dispenser.replenish_cash(amount)
        print(f"Deposit successful. New Balance: ${account.get_balance():.2f}")
        return True

# ---------------------------------------------------------------------------------------
# 4. Observer Pattern (Transaction Notification System)
# ---------------------------------------------------------------------------------------
class TransactionObserver(ABC):
    """
    Observer base class to be notified of transactions.
    """
    @abstractmethod
    def update(self, transaction): pass

class Bank(TransactionObserver):
    def update(self, transaction):
        print(f"[Bank] Transaction Recorded: {transaction.get_transaction_details()}")

# ---------------------------------------------------------------------------------------
# 5. Factory Pattern (For creating transaction objects)
# ---------------------------------------------------------------------------------------
class TransactionFactory:
    """
    Factory class for creating transactions.
    """
    @staticmethod
    def create_transaction(account, transaction_type, amount):
        return Transaction(account, transaction_type, amount)

# ---------------------------------------------------------------------------------------
# 6. Decorator Pattern (Logging Transactions Securely)
# ---------------------------------------------------------------------------------------
class SecureTransactionLogger:
    """
    Decorator for logging transactions securely.
    """
    @staticmethod
    def log(transaction):
        print(f"[Secure Log] {transaction.get_transaction_details()}")

# ---------------------------------------------------------------------------------------
# Core Classes
# ---------------------------------------------------------------------------------------
class UserAccount:
    def __init__(self, account_number: str, pin: str, balance: float):
        self.account_number = account_number
        self.pin = pin  # Should be stored securely in real-world applications
        self.balance = balance

    def authenticate(self, entered_pin: str):
        return self.pin == entered_pin

    def deposit(self, amount: float):
        self.balance += amount
        return True

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

class Card:
    def __init__(self, card_number: str, pin: str, linked_account: UserAccount):
        self.card_number = card_number
        self.pin = pin
        self.linked_account = linked_account

class CashDispenser:
    def __init__(self, initial_cash = 0):
        self.available_cash = initial_cash

    def dispense_cash(self, amount: float):
        if self.available_cash >= amount:
            self.available_cash -= amount
            return True
        return False
    def replenish_cash(self, amount: float):
        self.available_cash += amount

class Transaction:
    """
    Represents a banking transaction (Withdraw, Deposit).
    """
    def __init__(self, account: UserAccount, transaction_type: str, amount: float):
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    def get_transaction_details(self):
        return f"{self.timestamp} | {self.transaction_type} | Amount: ${self.amount:.2f}"
    
# ATM Class Implementing Singleton
class ATM(metaclass=SingletonMeta):
    def __init__(self, cash_dispenser: CashDispenser):
        self.cash_dispenser = cash_dispenser
        self.current_card = None
        self.state = IdleState()
        self.observers = []

    def change_state(self, state):
        self.state = state

    def insert_card(self, card, pin):
        self.state.insert_card(self, card, pin)

    def eject_card(self):
        self.state.eject_card(self)

    def perform_transaction(self, strategy, amount):
        self.state.perform_transaction(self, strategy, amount)

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, transaction):
        for observer in self.observers:
            observer.update(transaction)
        SecureTransactionLogger.log(transaction)

# Testing the implementation
cash_dispenser = CashDispenser()
cash_dispenser.replenish_cash(10000)
atm = ATM(cash_dispenser)
bank = Bank()
atm.add_observer(bank)

user_account = UserAccount("123456789", "1234", 5000)
user_card = Card("987654321", "1234", user_account)

atm.insert_card(user_card, "1234")
atm.perform_transaction(WithdrawStrategy(), 200)
atm.perform_transaction(DepositStrategy(), 500)
atm.eject_card()
