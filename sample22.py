#sample22.py
#coding: utf-8

data1 = [1,2,3,4,5]
data2 = data1
#data2 = list(data1)
data3 = data1.copy()

print("data1=",data1)
print("data2=",data2)
print("data3=",data3)

print("data1を変更")
data1[0] = 11

print("data1=",data1)
print("data2=",data2)
print("data3=",data3)
