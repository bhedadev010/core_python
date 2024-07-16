#if condition

a=1
if a>0:
    print("A is positive value")

#if-else condition

a=1
if a>0:
    print("A is positive value")
else:
    print("A is negative value")

#nested-if condition

a=1
if a>=0:
    if a==0:
        print("A is zero")
    else:
        print("A is positive value")
else:
    print("A is negative value")

#if-elif condition

a=10
if a>5:
    print("A is greater than 5")
elif a<5:
    print("A is smaller than 5")
else:
    print("Error in value")


#find min max from two numbers

a=int(input("Enter A :"))
b=int(input("Enter B :"))

if a>b:
    print("A is greater than B")
elif b>a:
    print("B is greater than A")
else:
    print("A is equal to B")


#find if a number is odd or even

a=int(input("Enter a number :"))

if a%2==0:
    print("Given number is even")
else:
    print("Given number is odd")


#find max num from 3 numbers

a=int(input("Enter A :"))
b=int(input("Enter B :"))
c=int(input("Enter C :"))

if a>b:
    if a>c:
        print("A is greatest")
    else:
        print("C is greatest")
elif b>a:
    if b>c:
        print("B is greatest")
    else:
        print("C is greatest")
else:
    print("Error in input")


#find avg of 3 sub marks and display result

a=int(input("Enter A :"))
b=int(input("Enter B :"))
c=int(input("Enter C :"))
avg=(a+b+c)/3

if avg>70:
    print("A+")
elif avg>=55:
    print("A")
elif avg>=45:
    print("B")
elif avg>=35:
    print("C")
else:
    print("FAIL")