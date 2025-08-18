# SUM of n natrual numbers using recursions 
def sum_of_natural(n):
    if n < 0:
        return f"Range must be positve."
    if n == 0:
        return 0
    return n + sum_of_natural(n-1)

print(sum_of_natural(10))
# 55
print(sum_of_natural(-10))
# Range must be positve.
print(sum_of_natural(0))
# 0
    
#------------------------------------------- 
# Greatest common divisior

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(16, 40))
# 8
print(gcd(12, 15))
# 3