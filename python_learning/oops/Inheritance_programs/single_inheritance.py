class parent:
    def greet(self):
        print("Hello from parent ")

class child(parent):
    def wish(self):
        print("Happy birthday!")

c = child()
c.greet()
c.wish()

#output:
# Hello from parent 
# Happy birthday!
