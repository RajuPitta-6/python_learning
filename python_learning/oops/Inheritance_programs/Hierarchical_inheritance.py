class parent:
    def property(self):
        print("parent : House")

class child1(parent):
    def skill(self):
        print("Child1 : painting")

class child2(parent):
    def skill(self):
        print("child2 : singing")

c1 = child1()
c1.property()
c1.skill()

# parent : House
# Child1 : painting

c2 = child2()
c2.property()
c2.skill()
# parent : House
# child2 : singing