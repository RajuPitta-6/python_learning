def is_Armstrong(Number):
    original = Number
    A_num = 0
    n = 0
    while(Number != 0):
        Number //= 10
        n += 1

    # Alternate to find number of digits in number
    # n = len(str(original))
    
    Number = original
    while(Number != 0):
        Digit = Number % 10
        Number //= 10
        A_num += Digit ** n # Alternate math.pow(Digit, n)

    if original == A_num:
        return True 
    else:
        return False
    
num = int(input("Enter a number to check its is Armstrong are not! :"))
print(f"{num} is Armstrong number" if is_Armstrong(num) else f"{num} is not a Armstrong number")

# Example Test cases

# Enter a number to check its is Armstrong are not! :153
# 153 is Armstrong number

# Enter a number to check its is Armstrong are not! :1634
# 1634 is Armstrong number

# Enter a number to check its is Armstrong are not! :1688
# 1688 is not a Armstrong number