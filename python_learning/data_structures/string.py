# creating string

# single quotes
s1 = 'Hello'

# double quotes
s2 = "World"

# Triple quotes (for multi-line strings)

s3 = '''
This is 
multi-line
string'''

print(s1, s2, s3)
#-------------------------------------------------
#string indexing and slicing
s = "Python"
#Indexing
print(s[0]) # first in stringa
print(s[-1]) # last in string
# slicing
print(s[0:4])
print(s[:3])
print(s[2:])
print(s[::2])
# output:
# P
# n
# Pyth
# Pyt
# thon
# Pto
#------------------------------------------------------------
# string operations
s1 = "Hello"
s2 = "World"

# concatenation
print(s1+" "+s2)
# output:
# Hello World

#Repetition
print(s1 * 3)
# output:
# HelloHelloHello

# Membership
print("H" in s1)
print("Z" not in s1)
# output:
# True
# True

#---------------------------------------
# String functions
s =" Python programming "
print(len(s))
# output :
# 20
print(s.lower())
# output :
# python programming
print(s.upper())
# output :
# PYTHON PROGRAMMING
print(s.strip())
# output :
# Python programming
print(s.replace("Python", "Java"))
# output :
# Java programming

print(s.split())
# output :
# ['Python', 'programming']

#------------------------------------------------
# String checking methods

s = "Hello123"
print(s.isalpha())
# False

print(s.isdigit())
# False

print("123".isdigit())
# True

print(s.startswith("He"))
# True

print(s.endswith("3"))
# True
#-------------------------------------------------------
# string formating
name ="Raz"
marks = "875"

# f-strings
print(f"Student {name} got {marks} marks.")
# Student Raz got 875 marks.

# format() method
print("Student {} got {} marks".format(name, marks))
# Student Raz got 875 marks

#------------------------------------------------------
# String iterating
s = "Python"
for char in s:
    print(char)

# P
# y
# t
# h
# o
# n