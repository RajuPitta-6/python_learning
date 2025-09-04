class Account:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} is Deposited successfully")
        else:
            print("Enter valid amount")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insuffient balance")
        else:
            self._balance -= amount
            print(f"{amount} is withdrawed successfully")

class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate = 0.5):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self._balance / 100) * self.interest_rate
        self._balance += interest
        
        print(f"interest amount {interest} is added! New balance : {self._balance}")

ac1 = Account("Raz", 2500)
sac1 = SavingsAccount("Ram", 8000)

ac1.deposit(100) # 100 is Deposited successfully
ac1.withdraw(300) # 300 is withdrawed successfully

sac1.deposit(2800) # 2800 is Deposited successfully
sac1.add_interest() # interest amount 54.0 is added! New balance : 10854.0