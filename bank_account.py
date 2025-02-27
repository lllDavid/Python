class Bank:
    def __init__(self):
        pass

    def get_(self):
        pass


class Customer:
    def __init__(self,id):
        self.id = id
        self.account_balance = 0

    def set_account_balance(self,amount):
        self.account_balance += amount

    def get_account_balance(self):
        print(f"You have {self.account_balance} in your account.")

    def withdraw_money(self,amount):
        if amount < self.account_balance:
            self.account_balance -= amount
            print(f"You withdraw {amount}")
        else:
            print("No enough in account balance")


c1 = Customer(1)
c1.set_account_balance(10000)
c1.get_account_balance()
c1.withdraw_money(1000)
c1.get_account_balance()