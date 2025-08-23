# Random password generator
import random
import string

def Random_password_generator(n):
    if n < 4:
        return "The password length must be 4 or more"
    
    password = []
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    numeric = random.choice(string.digits)
    symbol = random.choice(string.punctuation)
    password.extend([upper,lower,numeric,symbol])
    
    all_values = string.ascii_letters + string.digits + string.punctuation
    for p in range(n - 4):
        password.append(random.choice(all_values))

    random.shuffle(password)

    password = "".join(password)
    return password

def customized_password_generator():
    alpha = int(input("Enter number of alpha values in your password : "))
    numeric = int(input("Enter number of numeric values in your password : "))
    symbol = int(input("Enter number of special symbols values in your password : "))

    total = alpha + numeric + symbol
    if total < 4:
        return "The password length must be 4 or more"
    
    password = []

    for i in range(alpha):
        password.append(random.choice(string.ascii_letters))
    for i in range(numeric):
        password.append(random.choice(string.digits))
    for i in range(symbol):
        password.append(random.choice(string.punctuation))
    
    random.shuffle(password)
    password = "".join(password)

    return password

print("++++++++++++++Welcome to password generator+++++++++++++++")

choice = input("Do you want random password or customized password (r/c) : ")

if choice.lower() == 'r':
   length =  int(input("Enter your password size (must be not < 4) : "))
   print(f"Randomly generated password is : {Random_password_generator(length)}")
elif choice.lower() == 'c':
    print(f"Your customized password is : {customized_password_generator()}")
else:
    print("Enter an valid choice!")
'''
output_1:
++++++++++++++Welcome to password generator+++++++++++++++
Do you want random password or customized password (r/c) : r
Enter your password size (must be not < 4) : 12
Randomly generated password is : 1;)GNP]Rd{bo'''

'''
output_2:
++++++++++++++Welcome to password generator+++++++++++++++
Do you want random password or customized password (r/c) : c
Enter number of alpha values in your password : 4
Enter number of numeric values in your password : 4
Enter number of special symbols values in your password : 2
Your customized password is : 36/.27GlDE
'''