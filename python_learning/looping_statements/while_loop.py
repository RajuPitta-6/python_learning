# while loop basic syntax
'''
while condtion:
    set of statements'''

# baasic program with while loop

i = 1
while i < 5:
    print(i)
    i += 1 # Here using assignment  operator

# while loop with conditional statements and control statements
print("Program 2 :")
password = "Raz@000"
attempts = 3

while attempts != 0:
    trail = input("Enter password :")
    if trail == password:
        print("password is correct")
        break
    else:
        print("Password is incorrect ,try again!")
        attempts -=1
'''
Sample output 1:
1
2
3
4
Program 2 :
Enter password :raju1111
Password is incorrect ,try again!
Enter password :ram@44
Password is incorrect ,try again!
Enter password :king
Password is incorrect ,try again!

Sample output 2:
1
2
3
4
Program 2 :
Enter password :Bujji@1234
Password is incorrect ,try again!
Enter password :Raz@000
password is correct
'''