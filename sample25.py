#sample25.py
#coding: utf-8

data = [1,2,3,4,5]
print("現在のデータは",data)


print("data[::-1]をfor文で処理")

for i in data[::-1]:
	print(i)
print("data[::-1]は",data[::-1])

print("現在のデータは",data)

print("reversed(data)をfor文で処理")

for i in reversed(data):
	print(i)
print("reversed(data)は",reversed(data))

print("現在のデータは",data)
