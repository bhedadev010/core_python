
def test(a,b,c=3,d=2):
    print("A :",a," B :",b," C :",c," D :",d)

test(1,2)
#if default arguement is given from last it is not necessary to give every arguement


#if one default arguement is given then all variables must have default arguements
def test(a=10,b=20,c=30,d=40):
    print("A :",a," B :",b," C :",c," D :",d)

test()

def test(a=10,b=30,c=20,d=40):
    print("A :",a," B :",b," C :",c," D :",d)

test(b=100,d=200)

