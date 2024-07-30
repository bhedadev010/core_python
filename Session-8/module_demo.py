import udf

while True:

    print("*" * 40)
    print("1. OddEven")
    print("2. MaxOfTwo")
    print("3. MaxOfThree")
    print("4. Fibonacci")
    print("5. PrimeNumber")
    print("6. Exit")
    print("*" * 40)

    n = int(input("Enter your choice :"))
    print("*" * 40)

    if n==1:
        od=int(input("Enter Number :"))
        udf.odd_even(od)
        print("*" * 40)

    elif n==2:
        oe=int(input("Enter Number :"))
        op=int(input("Enter Number :"))
        udf.max_of_two(oe,op)
        print("*" * 40)

    elif n==3:
        a=int(input("Enter Number :"))
        b=int(input("Enter Number :"))
        c=int(input("Enter Number :"))
        udf.max_of_three(a,b,c)
        print("*" * 40)

    elif n==4:
        d=int(input("Enter Number :"))
        udf.fibo(d)
        print("*" * 40)

    elif n==5:
        o=int(input("Enter Number :"))
        udf.prime(o)
        print("*" * 40)

    elif n==6:
        print("Thanks for using our services")
        print("*" * 40)
        break

    else:
        print("Incorrect Choice.Try again")


