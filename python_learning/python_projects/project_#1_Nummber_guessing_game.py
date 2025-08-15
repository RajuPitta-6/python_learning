# Number Guessing game ...
import random
print("+"*5 +"Welcome to our number guessing game"+"+"*5)

Number = random.randint(1, 50)
level = input("Enter your level(easy/hard) :")
if level.lower() == 'easy':
        choice = 10
elif level.lower() == 'hard':
        choice = 5
else:
    print("Sorry invalid choise(default choose easy mode)")
    choice = 10

while choice > 0:
        guess_num = int(input("Enter your guessing number:"))
        if guess_num == Number:
            print("you won,Your guessed number is correct")
            break
        else:
            if guess_num > Number:
                print("Your guessing is too high")
            else:
                print("Your guessing is too low")
            choice -= 1
if choice == 0:
      print("Game over ,The correct number was :",Number)