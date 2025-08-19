class calculator:
    def __init__(self, num):
        self.num = num
    def square(self):
        return self.num ** 2
    
    def cude(self):
        return self.num ** 3
    
c = calculator(6)

print("square :",c.square())
print("Cube :",c.cude())

# output:
# square : 36
# Cube : 216