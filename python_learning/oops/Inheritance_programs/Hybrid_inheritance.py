class A:
    def feature1(self):
        print("Feature from A")

class B(A):
    def feature2(self):
        print("Feature from B")

class C(A):
    def feature3(self):
        print("feature from C")

class D(B, C):
    def feature4(self):
        print("feature from D ")
d = D()
d.feature1()
d.feature2()
d.feature3()
d.feature4()

# Feature from A
# Feature from B
# feature from C
# feature from D 