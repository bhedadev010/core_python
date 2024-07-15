#first
for i in range(1,6):
    print("*"*i)
for i in range(4,0,-1):
    print("*"*i)

#second
j=1
j=str(j)
for i in range(1,10):
    print(" "*(9-i),f" {j}"*i)
    j=int(j)+1
    j=str(j)

#third
j=1
for i in range(65,72):
    print(" "*(9-j),f" {chr(i)}"*j)
    j=j+1