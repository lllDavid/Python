from account import Account
from decimal import Decimal

account1 = Account(1, "David", Decimal(2000))
account2 = Account(2, "David2", Decimal(3000))

account1.deposit(Decimal(100))
account1.withdraw(Decimal(200))

print(account1+account2)