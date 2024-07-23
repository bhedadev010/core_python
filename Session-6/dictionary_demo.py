d = {12:"dev", 34:"wow", 54:"nice", "tops":" what"}

print(d)
print(d["tops"]) #same
print(d.get(12)) #same

print(d.items())

print(d.values())

print(d.keys())

#one arguement is compulsory which is key value
print(d.pop(12))
print(d)

#ACTS as .pop() in list
print(d.popitem())
print(d)

#UPDATE is used to update existing values from one to other and add the remaining new values
d = {12:"dev", 34:"wow", 54:"nice", "tops":" what"}
d1={13:"woww", 12:"niceee"}
d.update(d1)
print(d)