class math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def is_even(num):
        return num % 2 == 0
    

# No need to create object
print(math.add(5, 6))
print(math.is_even(5))

# Output:
# 11
# False