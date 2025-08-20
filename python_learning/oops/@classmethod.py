class student:
    school_name = "ZPH school"

    def __init__(self, name):
        self.name = name
        
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name 

# Befor changing
print(f"school name is :{student.school_name}")

student.change_school("XYZ school")
# After changing
print(f"school name is :{student.school_name}")

# output:
# school name is :ZPH school
# school name is :XYZ school