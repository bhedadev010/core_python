p = int(input("P :"))
r = float(input("R :"))
t = float(input("T :"))

si = (p*r*t)/100
ci = p*((1+r/100)**t-1)

print(si)
print(ci)
