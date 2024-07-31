class pizza:
    def order(self,kind):
        b1=0
        self.kind=kind
        print("Pizza type :",self.kind)
        if self.kind==("Simple" or "Cheese"):
            print("Sorry out of stock")
        else:
            if self.kind=="Simple":
                b1+=100
            else:
                b1+=130
    def order_2(self,siz):
        b2=0
        self.siz=siz
        print("Pizza size :",self.siz)
        if self.kind=="Simple":
            if self.siz=="S":
                b2+=30
            else:
                b2+=50
        else:
            if self.siz=="S":
                b2+=40
            else:
                b2+=60

    def bill(self):
        bill=b1+b2   #do this later
        print(bill)

piz1 = pizza()
piz1.order("Cheese")
piz1.order_2("S")
piz1.bill()