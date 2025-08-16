def greet(name):
    print(f"Hi {name}, How are you")

greet("sri-raj")
# Hi sri-raj, How are you
#-----------------------------
def add(a, b):
    c = a+b
    print(f"sum of two numbers are {c}")

add(55, 66)
# sum of two numbers are 121
#--------------------------------
def details(name, branch, sem ="III"):
    print(f"Name of the student is {name}")
    print(f"Branch is {branch},And He/She is studying  {sem} semster")

details("Raz","CS")
# Name of the student is Raz
# Branch is CS,And He/She is studying  III semster
details("Bujji","Mech","IV")
# Name of the student is Bujji
# Branch is Mech,And He/She is studying  IV semster

#-----------------------------------------

def add(*num):
    sum = 0
    for i in num:
        sum += i
    print(f"The total sum of numbers is {sum}")

add(5, 4, 7, 8, 9, 6)