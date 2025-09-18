def palindrome(x):
    size = len(x)
    for i in range(size // 2):
        if x[i] != x[size - (i+1)]:
            return False
    return True
    
string = input("Enter a string to check it is palindrome are not :")
print("It is palindrome " if palindrome(string.lower()) else "It is not a palindrome")

# --------------------------------------------------------------------------------------------
# method 2
    # if string[::-1] == string:
    #     return True
    # else :
    #     return False
# --------------------------------------------------------------------------------------------


# output:

# eg 1:
# Enter a string to check it is palindrome are not :razuzar
# It is palindrome 

# eg 2:
# Enter a string to check it is palindrome are not :razu
# It is not a palindrome