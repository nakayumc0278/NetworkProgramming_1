#challenge01.py
#coding: utf-8

a = {x for x in range(21)}
b = {x for x in range(21) if x % 2 == 0}
c = a - b

print("集合Aの表示")
print(a)

print("集合Bの表示")
print(b)

print("集合Cの表示")
print(c)