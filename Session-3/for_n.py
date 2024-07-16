#sum of all till N numbers

n=int(input("Enter N :"))
sum=0

for i in range(1,n+1,1):
    sum=sum+i

print(f"Sum of {n} numbers is : {sum}")