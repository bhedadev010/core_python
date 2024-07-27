
def odd_even(a):

    if a%2==0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")

def max_of_two(a,b):

    if a>b:
        print(f"{a} is max")
    elif b>a:
        print(f"{b} is max")
    else:
        print("both have same value")

def max_of_three(a,b,c):
    if a>b:
        if a>c:
            print(f"{a}is max")
        elif c>a:
            print(f"{c} is max")
        else:
            print(f"{a} and {c} are same")
    elif b>a:
        if b>c:
            print(f"{b}is max")
        elif c>b:
            print(f"{c} is max")
        else:
            print(f"{b} and {c} are same")
    else:
        print(f"{b} and {c} have same value")

def fibo(n):
    a=0
    b=1
    print(a,b,end=", ")
    while b<n:
        print(b,end=", ")
        a,b=b,a+b

def prime(a):
    if a%2!=0:
        for i in range(3,int(a/2)+1,2):
            if a%2==0:
                print(f"{a} not prime")
            else:
                print(f"{a} is prime")
                break
    else:
        print(f"{a} not prime")

