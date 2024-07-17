# for n numbers find sum

n=int(input("Enter N :"))
sum=0

for i in range(1,n+1):
    sum=sum+i

print(f"Sum of {n} numbers is : {sum}")

#fibonacci
#0 1 1 2 3 5 8 13

a,b=0,1
num=int(input("Enter num :"))
print(a,end=" ")
while b<num:
    print(b,end=" ")
    a,b=b,a+b

#guess num game

import random

number=random.randint(1,100)

while True:
    guess=int(input("\nEnter your guess between 1 to 100 :"))
    if guess+1==number or guess+2==number or guess+3==number or guess+4==number:
        print("You are close!!!")
    elif guess - 1 == number or guess - 2 == number or guess - 3 == number or guess - 4 == number:
        print("You are close!!!")
    elif guess<number:
        print("Your guess is smaller ")
    elif guess>number:
        print("Your guess is higher ")
    elif guess==num:
        print("You guessed the correct number!!!")


# find prime number

prime=int(input("Enter Num :"))

if prime%2!=0:
    for i in range(3,int(prime/2)+1,2):
        if prime%i==0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")
else:
    print("Number is not prime")

#while loop

num=int(input("Enter num :"))
sum=0
while num>0:
    sum=sum+num
    num=num-1
print(sum)