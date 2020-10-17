#sample28.py
#coding: utf-8

data = [1,2,3,4,5]
print("現在のデータ",data)

ndata = [n*2 for n in data if n!=3]
print("新しいデータ",ndata)
