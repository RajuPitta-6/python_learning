# To check the given number is prime or not 

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True
n =45
print(f"{n} is prime : {is_prime(n)}")
# 45 is prime : False
n = 5
print(f"{n} is prime : {is_prime(n)}")
# 5 is prime : True
n = 19
print(f"{n} is prime : {is_prime(n)}")
# 19 is prime : True

# To print prime numbers in give range 

def primes_in_range(start, end):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    return primes
        
start = 10
end = 50
print(f"primes numbers range between {start} and {end} is : {primes_in_range(start, end)}")
# primes numbers range between 10 and 50 is : [11, 13, 15, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]