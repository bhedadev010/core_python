#randomlu fill 1s and 0s in a 4*4 2d list,print list and find row and column with most num of 1s

import random

li = [[0]*4 for i in range(4)]

for i in range(0,4):
    for j in range(0,4):
        li[i][j] = random.randint(0,1)

print(li)
dic= dict()

for i in range(0,4):
    count = 0
    for j in range(0,4):
        if li[i][j]==1:
            count += 1
        dic[i] = count

max_one = max(dic,key=dic.get)
print(max_one)
