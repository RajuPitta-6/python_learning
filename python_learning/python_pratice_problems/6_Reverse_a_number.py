def reverse(Number):
    Reversed_num = 0
    while (Number != 0):
        Digit = Number % 10
        Reversed_num = (10 * Reversed_num) + Digit
        Number //= 10
    return Reversed_num
Number = int(input("Enter a number to Reverse : "))
rev_num = reverse(Number)

print(rev_num)

