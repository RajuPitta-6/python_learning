#Nested if condtion using for checking leap year or not

#Taking year as input
year = int(input("Enter year :"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year,"is a leap year")
        else:
            print(year , "is not a leap year ")
    else:
         print(year,"is a leap year")
else:
    print(year , "is not a leap year ")

'''
sample output:
Enter year :2024
2024 is a leap year'''
 