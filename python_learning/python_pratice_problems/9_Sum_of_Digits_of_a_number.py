def sum(Number):
    Total = 0
    while(Number != 0):
        Digit = Number % 10
        Total += Digit
        Number //= 10
    return Total

num = int(input("Enter a Number :"))
print(f"Sum of Digits of {num} is {sum(num)}")