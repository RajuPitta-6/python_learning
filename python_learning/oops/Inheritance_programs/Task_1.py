# Banking system
class BankAccount:
    def __init__(self,account_no,balance = 0):
        self.account_no = account_no
        self.balance = balance

    def Deposite(self, amount):
        if amount <= 0:
            print("Enter positive amount!")
        else:
            self.balance += amount
            print(f"Deposited {amount} New Balance : {self.balance}")
    def Withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdraw {amount} New Balance : {self.balance}")
    def show(self):
        print(f"Account_no : {self.account_no}, Balance : {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance=0, intrest_rate = 0.05):
        super().__init__(account_no, balance)
        self.intrest_rate = intrest_rate

    def Add_intrest(self):
        intrest = self.balance * self.intrest_rate
        self.balance += intrest
        print(f"Intrest Added , New Balance : {self.balance}")

ac_1 = SavingsAccount("SBI001",5000)

ac_1.Deposite(1000)
ac_1.Withdraw(333)
ac_1.Add_intrest()
ac_1.show()
# Deposited 1000 New Balance : 6000
# Withdraw 333 New Balance : 5667
# Intrest Added , New Balance : 5950.35
# Account_no : SBI001, Balance : 5950.35

ac_2 = BankAccount("SBI002",2000)
ac_2.Deposite(888)
ac_2.Withdraw(999)
ac_2.show()
# Deposited 888 New Balance : 2888
# Withdraw 999 New Balance : 1889
# Account_no : SBI002, Balance : 1889