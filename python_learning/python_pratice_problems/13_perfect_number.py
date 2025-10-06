def perfect_num(n):
    if n <= 0:
        return False
    divisor_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisor_sum += i
    if n == divisor_sum:
         return True
    else:
         return False
num = int(input("Enter a number to check it is perfect or not :"))
res = perfect_num(num)


if res:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

# Example outputs:

# Enter a number to check it is perfect or not :0
# 0 is not a perfect number

# Enter a number to check it is perfect or not :28
# 28 is a perfect number

# Enter a number to check it is perfect or not :496
# 496 is a perfect number

# num = int(input("Enter a number: "))
# print(f"{num} is a perfect number" if num > 0 and sum(i for i in range(1, num) if num % i == 0) == num else f"{num} is not a perfect number")