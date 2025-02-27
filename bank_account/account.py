from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Account:
    id: int
    owner: str
    balance: Decimal

    def deposit(self, value:Decimal):
        self.balance = self.balance + value
        print(f"Account balance increased by {value}. New balance {self.balance}")

    def withdraw(self, value:Decimal):
        if self.balance >= value:
            self.balance = self.balance - value
            print(f"Account balance decreased by {value}. New balance {self.balance}")
        else:
            print(f"Not enough funds")
    
    def __add__(self, other):
        return f"Accounts merged. Balance: {self.balance + other.balance}"
