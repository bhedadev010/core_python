#Create a file and write 10 random int in it , then based on odd and even write them in odd.txt and even.txt and prime

import random

data=open("data.txt","w")
for i in range(10):
    data.write(str(random.randint(1,100))+", ")
data.close()

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")

l=data.read().split(", ")[:-1]
for i in l:
    if int(i)%2==0:
        even.write(i+", ")
    else:
        odd.write(i+", ")

odd.close()
even.close()

odd=open("odd.txt","r")
even=open("even.txt","r")
print("Even num :"+even.read())
print("Odd num :"+odd.read())
even.close()
odd.close()

data=open("data.txt","r")
prime=open("prime.txt","w")
l=data.read().split(", ")[:-1]
print(l)

for i in l:
    if int(i) % 2 != 0:
        for j in range(3, int(int(i) / 2) + 1, 2):
            if int(i) % j == 0:
                break
        else:
            prime.write(str(i)+", ")

data.close()
prime.close()
prime=open("prime.txt",'r')
print(prime.read())
prime.close()

