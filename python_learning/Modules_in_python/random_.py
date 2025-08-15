# imports random module
import random 

# 1. random.random() generates a random float between 0.0 and 1.0(exclisive of 1)
print(random.random())
# 0.4718090679184245

# 2. random.uniform(a, b)  generates a float between a and b (both inclusive)
print(random.uniform(4, 9))
# 8.49785651195344

# 3. random.raadiant(a, b) generates a random integer between a and b(inclusive both)
print(random.randint(5, 12))
#10

# 4. random.randrange(start, stop, step) genertaes a random number from a range, similar range to range()
print(random.randrange(0, 10, 2))
# 6

# 5.random.choice(sequence) select one random element from a sequence
fruit = ['Apple','Banaba','mango']
print(random.choice(fruit))
# mango

# 6. random.choices(population weight = None,k = 1) select multiple random elements (with replcement-element can be repeated)
fruit = ['Apple','Banaba','mango']
print(random.choices(fruit, k=3))
# ['Banaba', 'Banaba', 'Apple']

print(random.choices(fruit, weights=[5, 2, 1], k=5))
# ['Apple', 'Apple', 'Banaba', 'mango', 'Apple']

# 7. random.shuffle(sequence) shuffle a sequence in a place 

card = [1, 2, 3, 4, 5, 6]
random.shuffle(card)
print(card)
# [2, 5, 4, 1, 3, 6]
