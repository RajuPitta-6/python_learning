# DICTINORY

# example for dictionary
person = {"Name":"Raz","Age":20,"City":"Vizag"}
Marks = {"Math":99,"Science":88,"English":96}
mixed = {"Name":"Raz","Age":20,"Is_student":True,"Skills":["Python","C"]}

#----------------------------------------------------------
#creating Dictonary

# Empty dictionary
my_dict = {}

# with values
my_dict = {"Name":"Raz","Age":20,"City":"Vizag"}

# Using dict() constructor
my_dict = dict(name = "Razu", Age = 21, city = "Vizag")

#----------------------------------------------
# Updating Dictionary items

person["Age"] = 22 # Update value for "Age"
person["Country"] = "India" # Add new key-value pair
print(person)
'''
output:
{'Name': 'Raz', 'Age': 22, 'City': 'Vizag', 'Country': 'India'}
'''
#---------------------------------------------------------

# Dictionary operations 
        # Adding elements 
person["Email"] = "raz@.com"

        # Removing elements
person.pop("City") # remove by key
person.popitem() # Remove last inserted key-value pair
del person["Age"] # Delete by key 
person.clear() # Remove all items 

        # searching 
print("name" in person) # true/false for key
print("Raz" in person.values()) #true/false for value

#---------------------------------------------------------
# Looping through a dictionary

for key in Marks:
    print(key, ":", Marks[key]) # print key and value

for key, value in Marks.items():
    print(key, ":", value) # Another way

#----------------------------------------------------------------
# Nested Dictinory
students = {
    "student1":{"Name":"Raz","Age":20},
    "student2":{"Name":"Ram", "Age":22}
}
print(students["student1"]["Age"]) # output :20

#------------------------------------------------------------------
# Dictionary methods 

print(Marks.keys())
print(Marks.values())
print(Marks.items())
'''
output:
dict_keys(['Math', 'Science', 'English'])
dict_values([99, 88, 96])
dict_items([('Math', 99), ('Science', 88), ('English', 96)])'''

# copying
new_marks = Marks.copy()

# length
print(len(Marks)) # output : 3