import json
import mmap

obj = '{"name": "Simy", "age":27}'

#parse string to json object
jsonObj = json.loads(obj)

print(type(obj))
print(type(jsonObj))

name = jsonObj["name"]
print(name)
print(jsonObj)


a = [i for i in range(0, 10)]
a.append(0)
print(a)

b = list(i for i in range(0, 10))
b.insert(0, -1)
print(b)

#add b into a
a.extend(b)
print(a)

target = 5
print("{} occurred {} times".format(target, a.count(target)), end="\n")
a = 1
b = 2

a,b = b,a

print(a, b)

