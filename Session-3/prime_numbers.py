n=int(input("Enter n :"))

if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print("N is not a prime number")
            break
    else:
        print(n," is a prime number")
else:
    print("N is not a prime number")

#prime numbers in a particular range