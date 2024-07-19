s=input("Enter String :")

al=0
nm=0
lw=0
up=0
sp=0
pr=0
for i in s:
    if i.isalpha():
        al=al+1

    elif i.isnumeric():
        nm=nm+1

    elif i.isspace():
        sp=sp+1
    elif i.isprintable():
        pr=pr+1

    if i.isupper():
        up=up+1
    elif i.islower():
        lw=lw+1

print("Total alpha :",al)
print("Total number :", nm)
print("Total space :", sp)
print("Total upper :", up)
print("Total lower :", lw)
print("Total Special char :", pr)
