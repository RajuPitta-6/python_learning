class Grandparent:
    def greet_gp(self):
        print("Hello from Grandparent")

class parent(Grandparent):
    def greet_p(self):
        print("Hello from parent")

class child(parent):
    def greet_c(self):
        print("Hello from child")

c = child()

c.greet_gp()
c.greet_p()
c.greet_c()

# Output:
# Hello from Grandparent
# Hello from parent
# Hello from child