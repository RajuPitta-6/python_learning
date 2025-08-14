# set

# Example 

num = {1, 2, 5, 4, 7, 9}
names = {'Raz','pavan','Bujji','vasu','firukpilla'}
mixed = {10, 4, 'Raz',True}

#---------------------------------------------
#creating set 

#Empty set 
my_set = set() # creates dict insted of set because of empty

# with values 
my_set = {11, 55, 'miiss',False}

# using set constructor

my_set = set((11, 55, 'miiss',False))

#------------------------------------------------------

# Adding elements 
fruits = {'Apple','Avacado','Banana','Mango','Cherry'}
fruits.add('Orange') # Add single element
fruits.update(['Papaya','Lemon']) # Adds mutiple elements

#------------------------------------------------------

#Removing elements

fruits.remove('Apple') # Removes by value (Error if not found)
fruits.discard('papaya') # Removes by value (No error if not found)
fruits.pop() # Removes a random element
fruits.clear() # Remove all elements

#------------------------------------------------------------
# set operations

A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B)) #{1, 2, 3, 4, 5}
print(A.intersection(B)) # {3}
print(A.difference(B)) #{1, 2}
print(A.symmetric_difference(B)) #{1, 2, 4, 5}

#----------------------------------------------

#set methods 

print(A.issubset(B)) #False
print(A.issuperset(B)) #False
print(A.isdisjoint(B)) #False

#----------------------------

# Frozen set(Immutable set)

frozen = frozenset([1, 2, 3])
print(frozen)

#-------------------------------------------------------

# LOpping through a set

for item in mixed:
    print(item)

#---------------------------------------------------

'''
NOTE :
sets are unordered 
so,no index'''

''' 
final outputs:
{1, 2, 3, 4, 5}
{3}
{1, 2}
{1, 2, 4, 5}
False
False
False
frozenset({1, 2, 3})
True
10
4
Raz
'''