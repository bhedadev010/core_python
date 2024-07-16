#0 1 1 2 3 5 8 13

'''
0=a
1=b . 1=a . 1=a
1=a+b . 1=b . 2=b
'''

a,b=0,1
n=int(input("Enter till what num you wanna see fibo : "))
print(a,end=" ")
while b<n:
    print(b,end=" ")
    a,b=b,a+b

