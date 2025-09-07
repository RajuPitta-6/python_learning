class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    # Getter method
    def get_balance(self):
        return f"Avl Balance :{self.__balance}"
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} is Deposited successfully")
        else:
            print("Enter valid amount")
    # setter method
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insuffient balance")
        else:
            self.__balance -= amount
            print(f"{amount} is withdrawed successfully")


ac1 = BankAccount("Raz", 2000)

print(ac1.get_balance())

ac1.deposit(111)
print(ac1.get_balance())

ac1.withdraw(222)
print(ac1.get_balance())

'''
Avl Balance :2000
111 is Deposited successfully
Avl Balance :2111
222 is withdrawed successfully
Avl Balance :1889
'''