class C:
    def getC(self,c):
        self.c = c

    def putC(self):
        print("C :",self.c)

class D(C):
    def getD(self,d):
        self.d = d

    def putD(self):
        print("D :",self.d)

class E(D):
    def getE(self,e):
        self.e = e

    def putE(self):
        print("E :",self.e)

print("\n\nMultilevel :")
e1 = E()
e1.getE(10)
e1.getC(20)
e1.getD(30)
e1.putE()
e1.putC()
e1.putD()