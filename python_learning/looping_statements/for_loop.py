#Looping through a list
l = ['Apple','Banana',"Avacado"]
print("Frist program output :")
for i in l:
    print(i)

# Looping through range 
print("second program output :")
for i in range(5):
    print(i)

# for loop with else
print("Third program output :")
for i in l:
    print(i)
else:
    print("List is completed")

'''
output:
Frist program output :
Apple
Banana
Avacado
second program output :
0
1
2
3
4
Third program output :
Apple
Banana
Avacado
List is completed
'''