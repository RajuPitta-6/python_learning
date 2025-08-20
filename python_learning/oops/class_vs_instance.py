class student:
    school_name = "ZPH school" # class variable (same for all)

    def __init__(self, name, age):
        self.name = name #Instance variable
        self.age = age

# creating objects

s1 = student("Raz", 23)
s2 = student("Mama", 25)

print(f"Name :{s1.name} Age : {s1.age}, School{s1.school_name}")
print(f"Name :{s2.name} Age : {s2.age}, School{s2.school_name}")

# output:
# Name :Raz Age : 23, SchoolZPH school
# Name :Mama Age : 25, SchoolZPH school

# Note:
# School name is same two students