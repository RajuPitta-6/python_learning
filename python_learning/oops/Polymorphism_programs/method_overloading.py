# method overloading example using default arguments

class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

cal = Calculator()
print(cal.add())
print(cal.add(5, 4))
print(cal.add(1, 5, 9))
# 0
# 9
# 15

# method overloading example using *args

class Summation:
    def add(self, *nums):
        return sum(nums)
    
s = Summation()

print(s.add())
print(s.add(4, 5, 7, 2, 9))
print(s.add(4, 3))

# 0
# 27
# 7