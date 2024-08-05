li = [10,20,30,10,20,30,40,50,50]
print(li)
dic = dict()

for i in li:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

a = list(dic.keys())
print(a)