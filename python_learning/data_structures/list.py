# LIST in python

#EXample for list 

fruits = ['Apple',"Banana","Mango"]
numbers = [1,2,3,4,5]
mixed = [10,8,'Raz',True]

#------------------------------------------------
#creating lis
# Empty list
my_list = []

# with values
my_list = [10,8,'Raz',True]

# using list() constructor
my_list = list((10,8,'Raz',True, 'python'))

#---------------------------------------------
#Accessing List items 

print(fruits[0]) # Apple (First item in the list)
print(fruits[-1]) # mango (last item in the list)

#-----------------
#updating List items 

fruits[1] = "Grapes"
print(fruits) # adds grapes to the first index

#---------------------------------------------

#List operations

    #Adding elements
fruits.append("orange") # Adds at the end
fruits.insert(1,"Kiwi") # Adds at specific index
fruits.extend(["papaya","lemon"]) # Adds multiple items

    #Removing elements
fruits.remove("Apple") # Removes by the value
fruits.pop(2)  #removes by index
fruits.clear() # removes all 

    #searching
print(fruits.index("Banana")) #Get index of Banana
print("mango" in fruits)  #True/False

   #slicing
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4]) # 2, 3, 4
print(numbers) # 1, 2, 3
print(numbers[::2]) # 1, 2, 3, 4, 5

    #sorting
numbers.sort() #sort in ascending order
numbers.sort(reverse=True) #sort in descending order

    #copying
new_list = numbers.copy()

    #counting
print(numbers.count(1)) # count occurrence of 1 in the number list

#-----------------------------------------------------------

# Looping through a list

for items in mixed:
    print(items)

#----------------------------------------------

#Nested list
N_nums = [[1, 2],[3, 4],[5, 6]]
print(N_nums[1][0]) # 3