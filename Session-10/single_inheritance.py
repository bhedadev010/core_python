class A:
    def getA(self,a):
        self.a = a

    def putA(self):
        print("A :",self.a)

class B(A):
    def getB(self,b):
        self.b = b

    def putB(self):
        print("B :",self.b)

print("Single :")
b1 = B()
b1.getB(10)
b1.getA(20)
b1.putB()
b1.putA()