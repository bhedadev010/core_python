import random

data = open("data.txt","w")

for i in range(10):
    data.write(str(random.randint(1,100))+", ")
data.close()
data = open("data.txt","r")
l = data.read().split(", ")[:-1]

odd = open("odd.txt","w")
even = open("even.txt","w")
prime = open("prime.txt","w")

for i in l:
    if int(i)%2==0:
        even.write(str(i)+", ")
    else:
        odd.write(str(i)+", ")

for i in l:
    if int(i)%2!=0:
        for j in range(3,int(int(i)/2)+1,2):
            if int(i)%j==0:
                break
            else:
                prime.write(str(i)+", ")

even.close()
odd.close()
prime.close()
even = open("even.txt",'r')
odd = open("odd.txt",'r')
prime = open("prime.txt",'r')

print("Even num :"+even.read())
print("Odd num :"+odd.read())
print("Prime num :"+prime.read())
