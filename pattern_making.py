#left-sided pyramid

for i in range(1,10):
    print("*"*i)

#right-sided pyramid

for i in range(1,10):
    print(" "*(9-i),"*"*i)

#pyramid

for i in range(1,10):
    print(" "*(9-i)," *"*i)

#ASCII left-sided pyramid

j=1
for i in range(65,75):
    print(chr(i)*j)
    j=j+1

#ASCII right-sided pyramid

j=1
for i in range(65,72):
    print(" "*(9-j),chr(i)*j)
    j=j+1

#ASCII pyramid





#Numbers left-sided pyramid

j= str(1)
for i in range(1,10):
    print(j*i)
    j=int(j)+1
    j= str(j)

#Numbers right-sided pyramid

j=1
j=str(j)
for i in range(1,10):
    print(" "*(9-i),j*i)
    j=int(j)+1
    j=str(j)

#Numbers pyramid

j=1
j=str(j)
for i in range(1,10):
    print(" "*(9-i),f" {j}"*i)
    j=int(j)+1
    j=str(j)