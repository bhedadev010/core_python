n = int(input("Enter N :"))
sum=0
if n<=0:
    print("wrong input")
else:
    for i in range(1,n+1,1):
        sum+=i
    print(sum)