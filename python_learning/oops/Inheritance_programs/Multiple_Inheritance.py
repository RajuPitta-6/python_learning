class A:
    def feature_a(self):
        print("Feature A")

class B():
    def feature_b(self):
        print("Feature B")

class C(A, B):
    def feature_c(self):
        print("Feature C")

c = C()

c.feature_a()
c.feature_b()
c.feature_c()

# Output:
# Feature A
# Feature B
# Feature C