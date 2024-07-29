h = int(input(" h :"))
r = int(input(" r :"))

if h<=40:
    print("wage :",h*r)
else:
    print("wage :",(h-40)*(0.5*r))