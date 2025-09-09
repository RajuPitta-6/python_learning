# Data Abstraction

class Student:
    def __init__(self, name, marks):
        # private variable
        self.__name = name
        self.__marks = marks

    def get_info(self):
        return f"Name : {self.__name}, Marks: {self.__marks}"
    
    def update_marks(self, new_marks):
        if new_marks > 0:
            self.__marks = new_marks
        else:
            print("Invalid marks!")

# Usage
s1 = Student("Raz", 89)
print(s1.get_info()) # Internal storage  details hide
# Name : Raz, Marks: 89
s1.update_marks(99)
print(s1.get_info())
# Name : Raz, Marks: 99
'''
Data abstraction means it hides internal data storage details and provides simple method to user'''
