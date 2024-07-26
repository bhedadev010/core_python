#fibo

n=100
a=0
b=1
print(str(a)+", "+str(b),end=", ")

while b<n:
    print(str(b),end=", ")
    a,b=b,a+b

#prime

n=19

if n%2==0:
    print("no")
else:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print("no")
        else:
            print("\n prime")
            break

n=5

for i in range(1,n+1):
    print("*"*i)

n=5

for i in range(1,n+1):
    print(" "*(9-i),"*"*i)

for i in range(1,n+1):
    print(" "*(9-i),"* "*i)



