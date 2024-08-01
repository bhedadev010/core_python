class C:
    def show(self):
        print("class c")

class D(C):
    def show(self):
        super().show()
        print("class d")

class E(C):
    def show(self):
        super().show()
        print("class e")

class F(D,E):
    def show(self):
        super().show()
        print("class f")

f1 = F()
f1.show()

# f -> d -> e -> c
