class Student:
    def getData(self,fname,lname):
        print("GetData called")
        self.f=fname
        self.l=lname
    def putData(self):
        print("PutData called")
        print("First Name :",self.f)
        print("Last Name :",self.l)


s1=Student()

s1.getData("Dev","Bheda")
s1.putData()