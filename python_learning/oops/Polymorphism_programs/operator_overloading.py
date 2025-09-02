# Example for operator overloading 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Overloading + operator

    def __add__(self, other):
        return Student("Total", self.marks + other.marks)
    
    # Overloading == operator

    def __eq__(self, other):
        return self.marks == other.marks
    
    # Overloading > operator

    def __gt__(self, other):
        return self.marks > other.marks

    # overloading str() to print object properly
    def __str__(self):
            return f"Name : {self.name} , marks : {self.marks}"
    


s1 = Student("Raz", 55)
s2 = Student("BM", 77)
s3 = Student("frnd", 67)

total = s1 + s2
print(total)
print(s1 < s2)
print(s2 == s3)
print(s2 > s3)

'''
output :
Name : Total , marks : 132
True
False
True
'''