#sample30.py
#coding: utf-8

data = [
	["東京",32,25],
	["名古屋",28,21],
	["大阪",27,20],
	["京都",26,19],
	["福岡",27,22]
]

print("現在のデータ",data)

for dat in data :
	print("都市別",dat)
	
	for i in dat:
		print(i,end="\t")
	print()

print(data[0][0],"最高気温",data[0][1],"最低気温", data[0][2])

