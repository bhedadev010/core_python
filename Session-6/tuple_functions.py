t = (1,2,4,6,True,'tops',1,54,[100,200,300])

print(t)

#Only two functions are available for tuple
print(t.count(1))

print(t.index(6))

print(t[8])

#Loophole is there as list functions can be used on list present inside tuple
t[8].append(400)

print(t[8])

for i in t:
    print(i)

print('tops'in t)