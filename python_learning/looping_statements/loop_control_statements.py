# while loop with control statment (break)
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
output:
Enter password :Bujji@1234
Password is incorrect ,try again!
Enter password :Raz@000
password is correct
'''

#While loop with continue satement

i = 1
while i < 7:
    if i == 3:
        i +=  1
        continue  
    else :
        print(i)
        i += 1
'''
output:
1
2
4
5
6
'''