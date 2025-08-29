class Animal:
    def sound(self):
        print("Animals makes different sounds")

class Dog(Animal):
    def sound(self): # overriding the parent class method
        print("Dog sounds bark")

class Cat(Animal):
    def sound(self): # overriding the parent class method
        print("Cat sounds meow")


a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()

# Animals makes different sounds
# Dog sounds bark
# Cat sounds meow
