#1. it is complusory to add arbitary constant at the end


#2. when a single star(*d) is added it works as a tuple which can take multiple arguements

def test(a,b,c,*d):
    print("A :", a, " B :", b, " C :", c, " D :", d)

test(1,2,3,4,5,6,7)


#3. when two star(**e) is added it works as a dict() which will store arguements in "key and value" pair

def test(a=4,b=3,c=2,*d,**e):
    print("A :", a, " B :", b, " C :", c, " D :", d," E :",e)

test(1,2,3,4,5,6,7,x=10,y=20,z=30)


#to convert tuple into list write list(d) inside function

def test(a,b,c,*d):
    d=list(d)
    print("A :", a, " B :", b, " C :", c, " D :", d)

test(1,2,3,4,5,6,7)


# if you give default values to a,b,c and give key-value pair to **e , in this scenario it is impossible to
#assign value to *d