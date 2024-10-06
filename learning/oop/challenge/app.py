from bank_account import *

acc1 = BankAccount(1000, "Joe Bloggs")
acc2 = BankAccount(1500, "Jan Doe")
acc3 = InterestRewardsAcct(1500, "Mark Smith")
acc4 = SavingAcct(500, "Alex Taylor")

acc1.get_balance()
acc1.deposit(20)
acc1.withdraw(500)
acc1.transfer(acc2, 200)

acc3.get_balance()
acc3.deposit(100)
acc3.transfer(acc1, 100)

acc4.get_balance()
acc4.withdraw(500)
acc4.withdraw(50)
