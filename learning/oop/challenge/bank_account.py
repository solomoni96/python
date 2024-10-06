class BankAccount:
    def __init__(self, initial_amount, acc_name):
        self.balance = initial_amount
        self.name = acc_name
        print(f"Account: '{self.name}' created.\nBalance: £{self.balance}\n")

    def deposit(self, amount):
        self.balance += amount
        print('Deposit Complete ✅')
        self.get_balance()
        
    def get_balance(self):
        print(f"Account: '{self.name}' current balance is £{self.balance:.2f}\n")
        
    def get_name(self):
        print(f"Account: '{self.name}' current balance is £{self.balance:.2f}\n")
        
    def transfer(self, acc, amount):
        try:
            print(f"******\n\nBeginning transfer to {acc.name}'s account 💸 💸 💸")
            self.viable_transaction(amount)
            self.withdraw(amount)
            acc.deposit(amount)
            print('Transfer Complete ✅\n\n******\n')
        except BalanceException as error:
            print(f"Transfer interrupted ❌\n{error}\n")
       
    def viable_transaction(self, amount):
        if (self.balance >= amount):
            return
        else:
            raise BalanceException(
                f"Transaction amount requested (£{amount}) exceeds current balance."
            )
        
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print('Withdrawal Complete ✅')
            self.get_balance()
        except BalanceException as error:
            print(f"Withdrawal interrupted ❌\n{error}\n")

class BalanceException(Exception):
    pass

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        amount_with_interest = amount * 1.05
        super().deposit(amount_with_interest)
        
class SavingAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acc_name):
        super().__init__(initial_amount, acc_name)
        self.fee = 5
        
    def withdraw(self, amount):
        try:
            withdrawal_amount = amount + self.fee
            self.viable_transaction(withdrawal_amount)
            self.balance -= withdrawal_amount
            print('Withdrawal Complete ✅')
            self.get_balance()
        except BalanceException as error:
            print(f"Withdrawal interrupted ❌\n{error}\n")
