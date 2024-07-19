n=input("Enter your name :")

uc=0
lc=0
al=0
nm=0
sp=0
sl=0


for i in n:
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        nm=nm+1
    elif i.isspace():
        sp=sp+1
    elif i.isprintable():
        sl=sl+1
    if i.isupper():
        uc=uc+1
    elif i.islower():
        lc=lc+1

print("ALPHABETS :",al)
print("NUMBERS :",nm)
print("UPPERCASE :",uc)
print("LOWERCASE :",lc)
print("SPACE :",sp)
print("SPECIAL SYMBOLS :",sl)