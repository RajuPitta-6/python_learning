# if and if else condtional statements 

# takings age as input

age = int(input("Enter your age :"))

# condtional statement

if age >= 18:
    print("Eligible for voting")

# Two way  condtional statement

if age < 18:
    print("You are minor")
else :
    print("You are major")

# Multi way conditional statement

if age <= 25:
    print("you are in young age")
elif age <=45:
    print("you are in middle age")
else:
    print("you are in old age ")