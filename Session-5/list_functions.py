l=[1,2,4,100,'tops',True,False,1] #TRUE is 1 and FALSE is 0
m=[1,4,3,6,5,7,5]

l.append(3)
print(l) #Adds a single element at the end of the list

l.pop(5)
print(l) #Removes a single element of whos index is passed

print(l.index('tops')) #Gives index value of the arguement given in brackets

print(l.count(1)) #Counts the occurance of a given arguement in the list

# l.clear()
# print(l) #Delete all the elements of the list

m=l.copy()  #Copies the list in the list it points to
m.append('dev')
print(m)

l.insert(3,'wow')  #Inserts a given object to the given index of the list
print(l)

l.remove('wow') #Deletes the object which is passed from the list
print(l)

l.reverse()
print(l)

l.__delitem__(6) #Deletes the object from the index passed as arguement
print(l)

l.extend(m) #Adds an entire list at last of former list
print(l)


