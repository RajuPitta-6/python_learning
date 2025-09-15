def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print("Factorial of 3 is : ",factorial(3))
print("Factorial of 5 is : ",factorial(5))
print("Factorial of 10 is : ",factorial(10))
print("Factorial of 15 is : ",factorial(15))

# Factorial of 3 is :  6
# Factorial of 5 is :  120
# Factorial of 10 is :  3628800
# Factorial of 15 is :  1307674368000