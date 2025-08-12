#Tasks taken from chat GPT

# Beginner Level

# Store your friends’ names in a list and print them one by one.

friends = ['razu','Arun','Bujji','mama','sai']
for friend in friends:
    print(friend)

# Find the sum of all numbers in a list using a loop.

num = [1, 4, 7, 8, 4, 9, 4, 22, 77]
sum = 0
for i in num:
    sum += i
print(sum)

# Reverse a list without using the built-in reverse() function.

n = len(num)
m = n-1
for i in range(n // 2):
    num[m-i],num[i] = num[i],num[m-i]
print(num)

# Count the frequency of a specific number in a list.

target = 4

count_4 = num.count(target)
print(count_4)

# Check if an element exists in the list or not.

print(4 in num)

# Intermediate Level

# Remove duplicates from a list (keep original order).
num2 = []
for i in num:
    if i in num2:
        continue
    else:
        num2.append(i)
print(num2)

# Find the second largest number in a list without using max() twice.
f = float('-inf')
s = float('-inf')
for num in num2:
    if num > s :
        s = f
        f = num
    elif num > s and num != f:
        s = num
print("second largest number is :",s)

# Merge two lists and remove duplicates.

list_1 = [1, 5, 8, 4, 6, 6]
list_2 = [4, 5, 7, 3, 8]

merged = list_1 + list_2
u_merged = []
for item in merged:
     if item not in u_merged:
         u_merged.append(item)
print(u_merged)

# Split a list into two halves.

mid = len(u_merged) // 2

first_half = u_merged[:mid]
second_half = u_merged[mid:]

print("first half of the list is :",first_half)
print("second half of the list is :",second_half)