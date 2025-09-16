def fibonacci_series(first, second, n):
    if n <= 0:
        print("Number of terms must be greater than 0")
        return
    series = []
    if n >= 1:
        series.append(first)
    if n >= 2:
        series.append(second)

    for i in range(n-len(series)):
        next_num = first + second
        series.append(next_num)
        first = second
        second = next_num
    return f"Fibonacci series of {n} terms is {series}"

print("***** Welcome to fibonacci series generator *****\n")
first = int(input("First number:"))
second = int(input("second number:"))
n = int(input("Enter how many terms you want :"))

result = fibonacci_series(first, second, n)
print(result)

# Output:
'''
***** Welcome to fibonacci series generator *****

First number:0
second number:1
Enter how many terms you want :10
Fibonacci series of 10 terms is [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''