
n = 73

if n%2!=0:  # checks for odd or even
    for i in range(3,int(n/2)+1,2):  # runs a loop for dividing odd nums
        if n%i==0:
            print("num aint prime")

        else:
            print("prime")
            break
else:
    print("num aint prime")