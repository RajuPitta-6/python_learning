class Student:
    def __init__(self, name, roll, marks):
        # public attributes
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Name : {self.name}, Roll_no : {self.roll}, Marks : {self.marks}")

# ----------------------------------------
# usage

s1 = Student("Raz", 23, 875)
s2 = Student("Mama", 16, 923)

# public --> Direct access
print(s1.name)
# Raz

# public --> Direct modification 
s1.marks = 999
print(s1.marks)
# 999

s1.display()
s2.display()
# Name : Raz, Roll_no : 23, Marks : 999
# Name : Mama, Roll_no : 16, Marks : 923