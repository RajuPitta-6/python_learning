# class with attributes
class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#creating object
d = dog("Tommy", 10)

print("Dog name is",d.name)
print("Dog age is",d.age)

# Dog name is Tommy
# Dog age is 10