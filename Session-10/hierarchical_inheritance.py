class I:
    def getI(self,i):
        self.i = i

    def putI(self):
        print("I :",self.i)

class K(I):
    def getK(self,k):
        self.k = k

    def putK(self):
        print("K :",self.k)

class J(I):
    def getJ(self,j):
        self.j = j

    def putJ(self):
        print("J :",self.j)

print("\n\nHierarchical :")
k1 = K()
j1 = J()
k1.getK(10)
k1.getI(20)
j1.getJ(30)
j1.getI(40)
k1.putK()
k1.putI()
j1.putJ()
j1.putI()