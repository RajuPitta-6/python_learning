# Tuple in python 

#Example for tuple 

fruits = ('Avacado','Berry','cherries')

numbers = (1, 2, 3, 4, 5)
mixed = (1, 7, 'raz', False)

#--------------------------------
# creating Tuples

#Empty tuple
my_tuple = ()

# With values
my_tuple = ('Bujji', False, 1)

# Using tuple() constructor
my_tuple = tuple((10, 45, 'Raz', True))

#--------------------------------------
# Accessing tuple items
print(fruits[1]) # Berry (second item in the tuple)
print(fruits[-1]) # cherries (Last item in the tuple)

#------------------------------------------
#Tuple operations 

    #searchin
print(fruits.index("Avacado")) # Get index of Avacado
print("Banana" in fruits) # True/False
     
     # Slicing 
num = (1, 2, 3, 4, 5, 6)

print(num[1:5]) #(2, 3, 4, 5)
print(num[::2]) #(1, 3, 5)

     #counting
print(num.count(1)) # count occurrence of 1 in tuple 

    # Length
print(len(num)) #6

#------------------------------------------
#Looping through a tuple

for  item in mixed:
    print(item)

#---------------------------
#Nested tuple

N_num = ((1, 2),(3, 4),(5, 6))
print(N_num[1][0]) #3

'''
Output :

Berry
cherries
0
False
(2, 3, 4, 5)
(1, 3, 5)
1
6
1
7
raz
False
3'''