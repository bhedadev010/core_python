n=int(input("Enter a number :"))

if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print("Number isn't a prime number ;/")
            break
    else:
        print("Number is a prime number :>")
else:
    print("Number isn't a prime number ;<")