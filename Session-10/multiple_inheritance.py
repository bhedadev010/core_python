class F:
    def getF(self,f):
        self.f = f

    def putF(self):
        print("F :",self.f)

class G:
    def getG(self,g):
        self.g = g

    def putG(self):
        print("G :",self.g)

class H(F,G):
    def getH(self,h):
        self.h = h

    def putH(self):
        print("H :",self.h)


print("\n\nMultiple :")
h1 =H()

h1.getH(10)
h1.getF(20)
h1.getG(30)
h1.putH()
h1.putF()
h1.putG()