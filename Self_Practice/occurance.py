n = input("Enter string :")
m = list(n)
m.sort()
print(m)
dic = dict()
o=len(n)

for i in range(0,o):
    if m[i] not in dic:
        dic[m[i]]=1
    else:
        dic[m[i]]+=1

for i in dic:
    print(f"{i}({dic[i]} time), ",end=" ")