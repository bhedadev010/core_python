file = open('poem.txt','r')
a = file.read()
a = a.split()
a.sort(key=len,reverse=True)
print(a[0])