
def test(a,b,c,d):
    print("A :",a," B :",b," C :",c," D :",d)

test(1,2,3,4)


#if one default arguement is given then all variables must have default arguements
def test(a=10,b=20,c=30,d=40):
    print("A :",a," B :",b," C :",c," D :",d)

test()

def test(a=10,b=30,c=20,d=40):
    print("A :",a," B :",b," C :",c," D :",d)

test(b=100,d=200)

