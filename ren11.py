#ren11.py
#coding: utf-8

data = [74,85,69,77,81]

print("テストの点は",data)

list_d = []
list_d = [d for d in data if d >= 80]

print("80点以上は",list_d)
print("80点以上の人数は",len(list_d),"人")
