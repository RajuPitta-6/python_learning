def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    

print(gcd(6, 9))
print(gcd(15, 90))
print(gcd(91, 15))

# 3
# 15
# 1