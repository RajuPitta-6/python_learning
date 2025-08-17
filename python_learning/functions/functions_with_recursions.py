# Recursions 
#------------------------------------------

# To find factorial using recursions 
def factoial(n):
    if n == 1:
        return 1
    else:
        return n * factoial(n-1)
    
print(factoial(5))
# Output : 120

print(factoial(10))
# Output : 3628800

#----------------------------------------
# Fibonacci series using recursions

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = 10
for i in range(10):
        print(fibonacci(i),end=" ")

# ------------------------------------------

def sum_natural(n):
    if n == 1:
        return n
    else:
        return n + sum_natural(n -1)

print("\n",sum_natural(10))
# output : 55
print(sum_natural(100))
# output : 5050