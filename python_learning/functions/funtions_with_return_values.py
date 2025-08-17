# functions with return values
def add_numbers(a, b):
    return a+b

total = add_numbers(36, 6)
'''output :
Sum of two numbers is 42
'''
print(f"Sum of two numbers is {total}")
#-------------------------------------------------
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return f"The factorial of {n} is {fact}"

fact = factorial(5)
# output : The factorial of 5 is 120
print(fact)
fact_2 = factorial(10)
print(fact_2)
# output : The factorial of 10 is 3628800
#---------------------------------------------------

def square_of_number(n):

    return f"square of {n} is {n * n}"

square = square_of_number(15)
print(square)
# output : square of 15 is 225