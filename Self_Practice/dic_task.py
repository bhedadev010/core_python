dic = {"brand": "Ford",  "model": "Mustang",  "year": 1964 }

dict = {
  1: 'Python',
  2: 'dictionary',
  3: 'example'
}

print(dic.items())

dic.pop("model")

dic["wow"]=2

print(dic)

print("no" in dic)

for i in dic:
    print(i)

dic.update(dict)
print(dic)

