class student:
    def __init__(self, Name, Marks):
        self.Name = Name
        self.__Marks = Marks

    def get_marks(self):
        return self.__Marks
    
    def update_marks(self, sub, n_marks):
        if sub in self.__Marks:
            if n_marks > 0:
                self.__Marks[sub] = n_marks
                return f"Update {sub} marks, New marks: {n_marks}"
            else:
                return f"Marks cannot accept as negative"
        else:
            return f"Subject {sub} not found!"

    def get_total(self):
        total = 0
        for i in self.__Marks.values():
            total += i
        return f"Total marks : {total}"


m1 = {"Maths" : 55, "science": 78, "Eng": 99}

s1 = student("Raz", m1)
print(s1.update_marks("social", 99))
print(s1.get_marks())
print(s1.update_marks("Maths", 89))
print(s1.get_total())
print(s1.get_marks())

'''
Output:
Subject social not found!
{'Maths': 55, 'science': 78, 'Eng': 99}
Update Maths marks, New marks: 89
Total marks : 266
{'Maths': 89, 'science': 78, 'Eng': 99}
'''