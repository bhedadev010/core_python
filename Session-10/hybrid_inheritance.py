class L:
    def getL(self,l):
        self.l = l

    def putL(self):
        print("L :",self.l)

class M(L):
    def getM(self,m):
        self.m = m

    def putM(self):
        print("M :",self.m)

class N(L):
    def getN(self,n):
        self.n = n

    def putN(self):
        print("N :",self.n)

class O(M,N):
    def getO(self,o):
        self.o = o

    def putO(self):
        print("O :",self.o)

print("\n\nHybrid :")
o1 = O()
o1.getO(10)
o1.getL(20)
o1.getM(30)
o1.getN(40)
o1.putL()
o1.putO()
o1.putM()
o1.putN()