# importing string module
import string

# Alphabets
print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz

print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.ascii_letters)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

#------------------------------------------
# Digits
print(string.digits)
# 0123456789

print(string.octdigits)
# 01234567

print(string.hexdigits)
# 0123456789abcdefABCDEF

#---------------------------------------
# Whitespace and punctuation
print(string.whitespace)
'''


'''
print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

#----------------------------------------------
# printable characters
print(string.printable)
'''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


'''

#-----------------------------------------------------
# Template strings

from string import Template

t = Template("Hello, $name! you got $marks marks.")
msg = t.substitute(name = "Raz", marks = 875)
print(msg)
# Hello, Raz! you got 875 marks.