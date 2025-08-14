# Tasks taken from chatGPT

# Beginner Level

# store your friends names in atuple and print them one by one .

friends = ('raz','Arun','Bujji','Mama','sai')
for friend in friends :
    print(friend)

'''
output :
raz
Arun
Bujji
Mama
sai
'''

# create a tuple with one element only and check its type.

s_element = ('Miss u')
print(type(s_element))
'''
output :
<class 'str'>
'''
# count how many times a specific value appears in a tuple.
num = (1, 7, 8, 9, 4, 1, 4, 5, 6, 1)
target = 4
count_4 = num.count(target)
print(count_4)
'''
output :
2+
'''
# find the index  of the first occirrence of a specific number.
print(num.index(8))
'''
output :
2
'''
#check if an element exists in the tuple
print(4 in num)
'''
output :
True
'''
# Intermediate Level

# concate two tuples.
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
m_tuple = tuple_1 + tuple_2
print(m_tuple)
'''
output :
(1, 2, 3, 4, 5, 6)
'''
# Repeat a tuple 3 times.
tup = (1, 'Raz') * 3
print(tup)
'''
output :
'''
# Tuple unpacking.
person = ('RAzu',20,'vizag')
name, age, city = person
print(name, age, city)
'''
output :
'''
# swap two numbers using tuple unpacking.
a, b = 5, 10
a, b = b, a
print(a, b)
'''
output :
'''
#Advance Level
#NEsted tuple access
Nested = (1, (2, 3),(4, (5, 6)))
print(Nested[2][1][0])
'''
output :
'''
#convert list to tuple and back to list after modification 
my_list = [10, 20, 30, 44]
my_tuple = tuple(my_list)
print(my_tuple)
my_list2 = list(my_tuple)
my_list.append(55)
print(tuple(my_list2))
'''
output :
'''