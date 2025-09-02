# Example 1 for Duck typing........

class car:
    def start(self):
        print("Car engine started")

class Bike:
    def start(self):
        print("Bike engine started")

class mechanic:
    def repiar(self, Vechile):
        Vechile.start()

c = car()
b = Bike()

m = mechanic()
m.repiar(c) # Car engine started
m.repiar(b) # Bike engine started


# Example 2 

class creditcard:
    def pay(self, amount):
        print(f"paid {amount} using credit card!")

class upi:
    def pay(self, amount):
        print(f"paid {amount} using upi!")


class payment_method:
    def process(self, payment_mode, amount):
        payment_mode.pay(amount)

cc = creditcard()
u = upi()

mode = payment_method()

mode.process(cc, 500)
mode.process(u, 900)\

# output:
# paid 500 using credit card!
# paid 900 using upi!